# Security policy

## Reporting

Do not open a public issue for a suspected vulnerability, malicious commit, or
leaked secret. Use GitHub’s private vulnerability-reporting feature when it is
enabled, or contact the maintainer through a private channel listed on the
maintainer’s GitHub profile.

Include the affected commit, file, reproduction details that do not expose a
secret, impact, and a suggested mitigation.

## Repository safety model

- Pull requests run with read-only contents permission and no repository
  secrets.
- CI uses `pull_request`, never `pull_request_target`, for untrusted changes.
- Review/scanning treats repository content as data and does not execute code
  found in a contribution.
- Main is protected by required pull requests and required status checks.
- Secret scanning and push protection should be enabled in GitHub settings.
- Signed commits are recommended for maintainers.

No scanner can prove that a repository is malware-free. These controls reduce
risk through static inspection, least privilege, review, and protected merges.
