.PHONY: check security validate benchmark package hooks

check: validate security benchmark

validate:
	python3 scripts/validate_repo.py

security:
	bash scripts/security_scan.sh .

benchmark:
	python3 scripts/validate_cases.py

package:
	bash scripts/build_skill.sh

hooks:
	git config core.hooksPath .githooks
