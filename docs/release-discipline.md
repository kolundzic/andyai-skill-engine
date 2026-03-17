# Release Discipline v0.1

## Rule

A release pack should be predictable, reviewable, and easy to overlay into the local repo without manual guesswork.

## Minimum Discipline

- same repo root on every ZIP
- release notes included
- trust example payloads included
- validation scripts included
- example skill payload included

## Local Deploy Pattern

```bash
unzip -o ~/Downloads/<zip-name>.zip -d ~/Documents/Projects
cd ~/Documents/Projects/andyai-skill-engine
git add .
git commit -m "<release message>"
git push
```

## Packaging Failure We Intentionally Avoid

Do **not** package ZIPs with a versioned root folder that creates a sibling directory instead of overlaying the existing repo.

Bad:
- `andyai-skill-engine-v0.4/`

Good:
- `andyai-skill-engine/`
