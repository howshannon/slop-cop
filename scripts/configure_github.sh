#!/usr/bin/env bash
set -euo pipefail

repo="${1:-howshannon/slop-cop}"
command -v gh >/dev/null || { echo "Install GitHub CLI first: https://cli.github.com/" >&2; exit 1; }
gh auth status >/dev/null

# Enable security features supported for the repository/plan.
gh api --method PATCH "repos/$repo" \
  -H "Accept: application/vnd.github+json" \
  -f 'security_and_analysis[secret_scanning][status]=enabled' \
  -f 'security_and_analysis[secret_scanning_push_protection][status]=enabled' \
  -F 'delete_branch_on_merge=true' || \
  echo "Some security settings could not be enabled through the API; enable them in Settings > Security."

# Protect main. For a solo-maintainer repo this requires a PR and status check
# but does not require a second person's approval. Change approvals_required to 1
# when a trusted second reviewer is available.
approvals_required="${APPROVALS_REQUIRED:-0}"
gh api --method PUT "repos/$repo/branches/main/protection" \
  -H "Accept: application/vnd.github+json" \
  --input - <<JSON
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["security-and-quality"]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": false,
    "required_approving_review_count": $approvals_required,
    "require_last_push_approval": false
  },
  "restrictions": null,
  "required_linear_history": true,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "block_creations": false,
  "required_conversation_resolution": true,
  "lock_branch": false,
  "allow_fork_syncing": true
}
JSON


printf 'Configured security features and main-branch protection for %s.\n' "$repo"
printf 'After the first successful workflow run, confirm the required check name in Settings > Rules.\n'
