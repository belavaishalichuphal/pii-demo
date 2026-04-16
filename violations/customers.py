"""
Customer data module — contains hardcoded PII for demo/testing purposes.
WARNING: This file intentionally contains PII violations.
"""

# Hardcoded customer records with PII
CUSTOMERS = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "email": "alice.johnson@gmail.com",
        "phone": "415-555-0192",
        "ssn": "532-78-4291",
        "address": "847 Maple Drive, Austin, TX 78701",
    },
    {
        "id": 2,
        "name": "Robert Chen",
        "email": "rchen1987@outlook.com",
        "phone": "(312) 555-7743",
        "ssn": "219-46-8803",
        "address": "12 Lakeview Blvd, Chicago, IL 60601",
    },
    {
        "id": 3,
        "name": "Maria Gonzalez",
        "email": "maria.g@yahoo.com",
        "phone": "305-555-2281",
        "ssn": "764-33-1920",
        "address": "399 Ocean Ave, Miami, FL 33101",
    },
]


def get_customer_by_email(email: str) -> dict | None:
    """Lookup a customer by their email address (PII)."""
    for c in CUSTOMERS:
        if c["email"] == email:
            return c
    return None


def export_all_customers() -> list[dict]:
    """Export all customer records including sensitive fields."""
    return CUSTOMERS
