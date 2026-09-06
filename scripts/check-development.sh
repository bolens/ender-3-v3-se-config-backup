#!/usr/bin/env bash
set -euo pipefail
root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
cd "$root"
# Match the shared fleet Markdown rules without an application dependency tree.
markdownlint-cli2 '*.md' 'docs/**/*.md' 'specs/002-development-environments/*.md'
shellcheck scripts/check-development.sh
ruff check scripts/development-container.py tests/test_development_container.py
python3 -m unittest discover -s tests -p 'test_development_container.py'
bash .githooks/pre-push
