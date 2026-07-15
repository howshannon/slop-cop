#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"
fail=0

say_error() { printf 'ERROR: %s\n' "$*" >&2; fail=1; }
say_warn()  { printf 'WARN: %s\n' "$*" >&2; }

# Never execute repository content. This scanner only reads files and parses shell syntax.
if find . -path ./.git -prune -o -type l -print | grep -q .; then
  find . -path ./.git -prune -o -type l -print
  say_error "symbolic links are not allowed without explicit review"
fi

# Hidden Unicode can conceal commands or identifiers.
python3 - <<'PYSCAN' || fail=1
from pathlib import Path
import sys
bad = {"\u200b", "\u200c", "\u200d", "\u2060", "\ufeff", "\u202e", "\u202d"}
found = []
for p in Path('.').rglob('*'):
    if not p.is_file() or '.git' in p.parts or 'dist' in p.parts:
        continue
    try:
        text = p.read_text(encoding='utf-8')
    except (UnicodeDecodeError, OSError):
        continue
    for n, line in enumerate(text.splitlines(), 1):
        chars = sorted({f'U+{ord(c):04X}' for c in line if c in bad})
        if chars:
            found.append(f"{p}:{n}: hidden Unicode {','.join(chars)}")
if found:
    print('\n'.join(found), file=sys.stderr)
    sys.exit(1)
PYSCAN

# Reject unexpected executables/binaries. Images and the packaged zip are intentionally excluded.
while IFS= read -r -d '' file; do
  case "$file" in
    ./.git/*|./assets/*|./dist/*|*.png|*.jpg|*.jpeg|*.webp|*.gif|*.svg|*.ico|*.zip|*.skill) continue ;;
  esac
  mime=$(file -b --mime-type "$file" 2>/dev/null || true)
  case "$mime" in
    text/*|application/json|application/x-yaml|application/xml|inode/x-empty) ;;
    *) say_error "unexpected non-text file: $file ($mime)" ;;
  esac
done < <(find . -path ./.git -prune -o -type f -print0)

# Static high-signal patterns. Exclude the scanner itself because it contains
# the patterns as data. Each expression is deliberately narrow to reduce noise.
patterns=(
  '(curl|wget)[[:space:]].*\|[[:space:]]*(sh|bash)'
  'base64[[:space:]]+(-d|--decode).*(sh|bash)'
  '(^|[^[:alnum:]_])(eval|exec)[[:space:]]*\('
  'os\.system[[:space:]]*\('
  'subprocess\.(Popen|run|call).*shell[[:space:]]*=[[:space:]]*True'
  'chmod[[:space:]]+\+s'
  '/dev/tcp/'
  'nc[[:space:]].*(-e|--exec)'
  'powershell.*(-enc|-encodedcommand)'
  'Invoke-Expression|FromBase64String'
  'rm[[:space:]]+-rf[[:space:]]+[/~]'
  'git[[:space:]]+config[[:space:]]+.*insteadOf'
)
for pattern in "${patterns[@]}"; do
  set +e
  matches=$(rg -n -i --hidden --glob '!.git/**' --glob '!dist/**' \
    --glob '!scripts/security_scan.sh' --glob '!.github/workflows/security.yml' "$pattern" . 2>&1)
  status=$?
  set -e
  if (( status == 0 )); then
    printf '%s\\n' "$matches"
    say_error "high-risk execution or obfuscation pattern found"
  elif (( status > 1 )); then
    printf '%s\\n' "$matches" >&2
    say_error "security pattern scan failed"
  fi
done

# Workflow safety and immutable action references.
for wf in .github/workflows/*.yml .github/workflows/*.yaml; do
  [[ -e "$wf" ]] || continue
  rg -n 'pull_request_target' "$wf" && say_error "pull_request_target is forbidden: $wf"
  while IFS= read -r line; do
    ref=${line#*@}
    ref=${ref%%[[:space:]#]*}
    [[ "$ref" =~ ^[0-9a-f]{40}$ ]] || say_error "GitHub Action is not pinned to a full SHA in $wf: $line"
  done < <(rg -o 'uses:[[:space:]]*[^[:space:]#]+@[^[:space:]#]+' "$wf" || true)
done

# Parse shell scripts but do not execute them.
while IFS= read -r -d '' script; do
  bash -n "$script" || say_error "shell syntax failed: $script"
done < <(find . -path ./.git -prune -o -type f \( -name '*.sh' -o -path './.githooks/*' \) -print0)

# Optional dedicated scanners, when installed locally or in a hardened runner.
if command -v gitleaks >/dev/null; then
  gitleaks detect --source . --no-banner --redact || fail=1
else
  say_warn "gitleaks not installed"
fi
if command -v semgrep >/dev/null; then
  semgrep scan --config p/secrets --config p/security-audit --error --metrics=off . || fail=1
else
  say_warn "semgrep not installed"
fi
if command -v trivy >/dev/null; then
  trivy fs --scanners vuln,secret,misconfig --exit-code 1 --severity HIGH,CRITICAL . || fail=1
else
  say_warn "trivy not installed"
fi
if command -v osv-scanner >/dev/null; then
  set +e
  osv_output=$(osv-scanner scan source -r . 2>&1)
  osv_status=$?
  set -e

  if (( osv_status == 0 )); then
    printf '%s\n' "$osv_output"
  elif grep -q "No package sources found" <<<"$osv_output"; then
    say_warn "osv-scanner skipped: no supported package manifests found"
  else
    printf '%s\n' "$osv_output" >&2
    say_error "osv-scanner found an issue or failed unexpectedly"
  fi
else
  say_warn "osv-scanner not installed"
fi

(( fail == 0 )) || exit 1
printf 'Static repository security checks passed.\n'
