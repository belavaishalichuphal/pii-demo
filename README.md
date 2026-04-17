# brix-pii-demo

Demo repository for testing PII detection and compliance scanning.

## Structure

### Original components

| Folder | Description |
|--------|-------------|
| `clean/` | Files with **no PII** — should pass all compliance checks |
| `violations/` | Files with **intentional PII** — should trigger compliance alerts |
| `mixed/` | Files with a **mix** of PII and clean data — partial violations |

### Mixed components (each has both clean and PII-containing files)

| Folder | Domain | Clean files | PII files |
|--------|--------|-------------|-----------|
| `hr-onboarding/` | HR | `onboarding_config.yaml`, `department_headcount.json` | `new_hires.csv` (name, email, phone, SSN, DOB, address, salary) |
| `crm-export/` | Sales/CRM | `pipeline_metrics.json`, `sales_config.yaml` | `contacts.py` (name, email, phone, SSN, address) |
| `support-tickets/` | Customer Support | `ticket_schema.yaml`, `sla_report.md` | `open_tickets.json` (name, email, phone, SSN, DOB, card number) |
| `billing-records/` | Finance/Payments | `invoice_config.yaml`, `revenue_summary.json` | `payment_records.csv` (name, email, phone, card number, CVV, address) |
| `medical-intake/` | Healthcare | `clinic_config.yaml`, `appointment_stats.json` | `patient_intake.py` (name, email, phone, SSN, DOB, address, medications — PHI) |
| `job-applications/` | Recruiting | `job_postings.json`, `hiring_funnel.md` | `applicants.csv` (name, email, phone, SSN, DOB, address) |
| `event-logs/` | Engineering/Ops | `log_config.yaml`, `system_events.json` | `user_activity.py` (name, email, phone, SSN, DOB, address in log fields) |
| `survey-responses/` | Customer Success | `survey_config.yaml`, `aggregate_results.json` | `individual_responses.csv` (name, email, phone, DOB) |
| `partner-contacts/` | Partnerships | `company_profiles.json`, `partnership_kpis.yaml` | `contact_directory.csv` (name, work/personal email, mobile, address, DOB) |
| `financial-reports/` | Finance | `budget_config.yaml`, `quarterly_summary.json` | `account_holders.py` (name, email, phone, SSN, DOB, bank account, routing number) |

## PII Types Covered

- Full names and email addresses
- Phone numbers and SSNs
- Physical mailing addresses
- Credit/debit card numbers

## Purpose

Used to validate PII detection logic in the brix compliance pipeline.
