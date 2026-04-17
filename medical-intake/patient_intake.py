"""
Patient intake records — WARNING: contains PHI/PII.
This file should be flagged by both HIPAA and PII compliance checks.
"""

# Intake forms collected at registration
PATIENT_RECORDS = [
    {
        "patient_id": "PT-0091",
        "full_name": "Eleanor Vance",
        "email": "eleanor.vance@gmail.com",
        "phone": "614-555-8830",
        "dob": "1962-09-11",
        "ssn": "372-88-4401",
        "address": "4402 Riverside Dr, Columbus, OH 43221",
        "insurance_id": "BCBS-7712-EV",
        "primary_condition": "hypertension",
        "medications": ["lisinopril 10mg", "amlodipine 5mg"],
        "emergency_contact_name": "Harold Vance",
        "emergency_contact_phone": "614-555-8831",
    },
    {
        "patient_id": "PT-0092",
        "full_name": "Omar Rashid",
        "email": "o.rashid@yahoo.com",
        "phone": "(773) 555-2291",
        "dob": "1978-04-03",
        "ssn": "491-23-6670",
        "address": "88 S Michigan Ave, Chicago, IL 60603",
        "insurance_id": "AETNA-0033-OR",
        "primary_condition": "type 2 diabetes",
        "medications": ["metformin 1000mg", "glipizide 5mg"],
    },
    {
        "patient_id": "PT-0093",
        "full_name": "Chloe Dupont",
        "email": "chloe.dupont88@hotmail.com",
        "phone": "504-555-7714",
        "dob": "1988-12-28",
        "ssn": "263-41-9920",
        "address": "12 Canal St, New Orleans, LA 70112",
        "insurance_id": "CIGNA-5519-CD",
        "primary_condition": "asthma",
        "medications": ["albuterol inhaler"],
    },
]


def lookup_patient(patient_id: str) -> dict | None:
    return next((p for p in PATIENT_RECORDS if p["patient_id"] == patient_id), None)


def search_by_ssn(ssn: str) -> dict | None:
    """Search by SSN — highly sensitive PII lookup."""
    return next((p for p in PATIENT_RECORDS if p.get("ssn") == ssn), None)
