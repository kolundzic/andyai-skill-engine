# First Release Checklist v1.0

Before creating the first visible GitHub release:

- confirm repo is public
- confirm `LICENSE` is Apache-2.0
- confirm `NOTICE` exists
- confirm `README` is polished
- confirm `VERSION` is correct
- confirm release notes exist
- run local checks:
  - `make validate`
  - `make check-pack`
  - `make test`
  - `make cli-smoke`
- confirm no accidental private files are present
- prepare release title and release body
