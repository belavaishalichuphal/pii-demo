# brix-pii-demo

Demo repository for testing PII detection and compliance scanning.

## Structure

| Folder | Description |
|--------|-------------|
| `clean/` | Files with **no PII** — should pass all compliance checks |
| `violations/` | Files with **intentional PII** — should trigger compliance alerts |
| `mixed/` | Files with a **mix** of PII and clean data — partial violations |

## PII Types Covered

- Full names and email addresses
- Phone numbers and SSNs
- Physical mailing addresses
- Credit/debit card numbers

## Purpose

Used to validate PII detection logic in the brix compliance pipeline.
