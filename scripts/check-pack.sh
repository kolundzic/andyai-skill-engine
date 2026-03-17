#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="${1:-.}"
for path in README.md RELEASE_NOTES_v1.0.md docs/testing.md docs/project-structure.md docs/quickstart.md docs/faq.md docs/release-checklist.md docs/v1-release-summary.md .gitignore LICENSE CONTRIBUTING.md CHANGELOG.md VERSION; do
  [ -f "${ROOT_DIR}/${path}" ] || { echo "Missing required file: ${path}"; exit 1; }
done
echo "Pack check passed."
