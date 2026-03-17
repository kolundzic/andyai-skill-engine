# Skill Model v0.2

## Definition

A skill is a structured, reusable execution unit that maps a known class of intent to a controlled output pattern.

## Skill Components

Each skill should define:
- id
- version
- title
- purpose
- input schema
- output schema
- execution instructions
- constraints
- compatibility targets
- trust metadata

## Why Skills Beat Raw Prompting

Raw prompting is flexible but chaotic.
Skills add:
- structure
- repeatability
- reviewability
- portability

## Example Mental Model

Prompt = one conversation move  
Skill = reusable operational object

## Skill Lifecycle

1. define
2. validate
3. test
4. run
5. record evidence
6. export
7. evolve

## Canonical Principle

**A good skill can survive a model swap because its structure is higher than the model call itself.**
