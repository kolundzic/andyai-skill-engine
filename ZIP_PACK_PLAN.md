# ZIP PACK PLAN v0.2

## Goal

Prepare clean ZIP deliverables for the same repo root:
`andyai-skill-engine/`

## Rule

For an existing repo, the ZIP must unpack directly over:
`~/Documents/Projects/`

so that files land inside:
`~/Documents/Projects/andyai-skill-engine`

## Packages

### 1. Repo Snapshot
Primary working ZIP for local repo overlay.

### 2. Release Pack
Mirror ZIP for fallback download.

## Canonical Deploy Model

1. download ZIP
2. unzip over `~/Documents/Projects`
3. `git add .`
4. `git commit`
5. `git push`

## Important Packaging Warning

Never use a versioned ZIP root such as:
- `andyai-skill-engine-v0.4/`

Always use:
- `andyai-skill-engine/`
