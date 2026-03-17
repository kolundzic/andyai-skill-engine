#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="${1:-.}"

echo "Checking pack at: ${ROOT_DIR}"

required_paths=(
  "README.md"
  "RELEASE_NOTES_v0.5.md"
  "docs/trust-model.md"
  "docs/release-discipline.md"
  "examples/skills/minimal_skill.json"
  "trust/skill-manifest.example.json"
  "trust/release-bundle.example.json"
  "scripts/validate-skills.py"
)

for path in "${required_paths[@]}"; do
  if [ ! -f "${ROOT_DIR}/${path}" ]; then
    echo "Missing required file: ${path}"
    exit 1
  fi
done

echo "Pack check passed."
