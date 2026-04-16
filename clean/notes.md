# Sprint Notes — Q1 2026

## Goals

- Complete compliance pipeline integration
- Achieve 95%+ PII detection accuracy on test dataset
- Reduce false positive rate below 2%

## Architecture Decisions

- PII scanning runs as an async job on document ingest
- Results are stored in the compliance schema, not alongside raw content
- Redaction is non-destructive — original content preserved in vault

## Open Questions

- How should we handle multi-language PII (e.g. Japanese names)?
- Do we need a separate allowlist for internal test data?

## Action Items

- [ ] Review regex patterns for SSN detection edge cases
- [ ] Add benchmark suite for large document batches
- [ ] Update runbook with new compliance check endpoints
