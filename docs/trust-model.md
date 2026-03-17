# Trust Model v0.1

## Purpose

The trust model defines the minimum metadata and release bundle expectations needed for a skill pack to be treated as reviewable and operationally serious.

## Trust Layers

1. **Skill payload trust**
   - required identity fields
   - declared inputs / outputs
   - declared constraints
   - trust metadata block

2. **Package trust**
   - expected repo root
   - required files present
   - no accidental versioned root folder

3. **Release trust**
   - release bundle manifest exists
   - referenced skills are listed
   - checks are recorded
   - release metadata is explicit

## Why This Matters

Trust is not magic.
Trust is:
- structure
- checks
- repeatability
- evidence that the pack is what it claims to be

## Current v0.5 Scope

This version does not yet implement signatures.
It establishes the first practical layer:
- example trust payloads
- pack checks
- release bundle structure
- validation script
