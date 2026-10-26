.PHONY: build check test verify
build:
	python3 scripts/build_readme.py
check:
	python3 scripts/check.py
test:
	python3 -m unittest discover -s tests -v
verify: check test
