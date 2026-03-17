#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="${1:-.}"
for path in README.md RELEASE_NOTES_v0.8.md docs/testing.md docs/project-structure.md .gitignore LICENSE CONTRIBUTING.md CHANGELOG.md; do
  [ -f "${ROOT_DIR}/${path}" ] || { echo "Missing required file: ${path}"; exit 1; }
done
echo "Pack check passed."
