#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="${1:-.}"
required_paths=(
  "README.md"
  "RELEASE_NOTES_v0.6.md"
  "docs/trust-model.md"
  "docs/release-discipline.md"
  "docs/cli-usage.md"
  "docs/dev-setup.md"
  "examples/skills/minimal_skill.json"
  "trust/skill-manifest.example.json"
  "trust/release-bundle.example.json"
  "scripts/validate-skills.py"
  "src/skill_engine/cli.py"
  "pyproject.toml"
)
for path in "${required_paths[@]}"; do
  if [ ! -f "${ROOT_DIR}/${path}" ]; then
    echo "Missing required file: ${path}"
    exit 1
  fi
done
echo "Pack check passed."
