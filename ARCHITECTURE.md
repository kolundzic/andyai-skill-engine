# Architecture v0.2

## System View

AndyAI Skill Engine has four major layers:

1. **Skill Definition Layer**
2. **Validation Layer**
3. **Orchestration Layer**
4. **Compatibility / Export Layer**

## 1. Skill Definition Layer

This layer defines what a skill is:
- identity
- intent
- inputs
- outputs
- constraints
- execution hints
- trust metadata

The goal is to describe a reusable unit without locking it to one vendor runtime.

## 2. Validation Layer

This layer checks:
- schema compliance
- required fields
- version discipline
- compatibility targets
- safe execution assumptions

Validation is what makes skills portable and reviewable.

## 3. Orchestration Layer

This is the operational brain:
- choose the skill
- resolve context
- bind inputs
- execute
- collect outputs
- store evidence
- return result

The orchestration layer is the master behavior layer of the system.

## 4. Compatibility / Export Layer

This layer transforms internal skill definitions into external ecosystem formats.

Examples:
- Copilot-friendly pack
- internal mission packs
- UI assistant packs
- agent runtime adapters

## Architectural Thesis

The master asset is **not** the prompt.
The master asset is **the structured skill definition + orchestration logic**.

## Minimal Flow

```text
User Intent
   ↓
Context Resolution
   ↓
Skill Match
   ↓
Input Binding
   ↓
Validation
   ↓
Execution
   ↓
Output + Evidence
   ↓
Compatibility Export (optional)
```

## Why This Wins

A stable skill engine:
- reduces prompt sprawl
- improves reuse
- allows governance
- supports trust and auditing
- creates an exportable product surface
