# AndyAI Skill Engine

## Core Definition

**AndyAI Skill Engine is a skill-based orchestration architecture for reusable, verifiable AI execution.**

It treats skills as portable execution units that can be defined once, validated, mapped to different runtimes, and reused across many workflows. The repo is the **master architecture**. Compatibility targets such as Copilot are export paths, not the source of truth.

## Key Principles

- skills are modular execution units
- orchestration stays above individual tools
- compatibility layers are adapters, not the core
- verification matters as much as execution
- reusable skill packs beat one-off prompt chaos

## Strategic Position

AndyAI Skill Engine sits in the emerging layer between:
- model providers
- agent runtimes
- workflow tools
- enterprise operational systems

Its purpose is to define a durable skill architecture that can survive model churn and tool churn.

## Repository Structure

```text
andyai-skill-engine/
├── README.md
├── ARCHITECTURE.md
├── MARKET_ANALYSIS.md
├── ROADMAP.md
├── SKILL_MODEL.md
├── ZIP_PACK_PLAN.md
├── RELEASE_NOTES_v0.3.md
├── PACKAGING_CHECKLIST.md
├── schemas/
│   └── skill.schema.json
├── examples/
│   ├── ui_skill_example.json
│   └── copilot/
│       └── minimal-skill-pack/
│           ├── skill.json
│           ├── prompt.md
│           └── README.md
├── diagrams/
│   └── skill-engine-flow.md
├── docs/
│   ├── copilot-mapping.md
│   └── repo-positioning.md
└── compat/
    └── copilot/
        └── README.md
```

## Why This Repo Matters

Most AI systems today optimize one of two things:
- raw model capability
- raw speed / infra efficiency

AndyAI Skill Engine focuses on a third layer:
- **execution structure**

That is where reusable business value gets stabilized.

## Current Release

This snapshot represents **v0.3 repo packaging discipline**, with:
- core repo definition
- skill model write-up
- compatibility path to Copilot
- example minimal skill pack
- packaging and release notes

## Canonical Line

**Copilot compatibility is an export path. AndyAI Skill Engine remains the master architecture.**
