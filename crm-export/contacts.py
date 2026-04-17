"""
CRM contact export — WARNING: contains raw PII from contact records.
This file should be flagged by PII scanning.
"""

# Exported contact records including personal details
CONTACTS = [
    {
        "contact_id": "cnt_001",
        "full_name": "Sandra Osei",
        "email": "sandra.osei@techcorp.com",
        "personal_email": "s.osei.personal@gmail.com",
        "mobile": "650-555-3382",
        "direct_line": "(650) 555-0047",
        "linkedin": "linkedin.com/in/sandraosei",
        "dob": "1983-07-14",
        "home_address": "1402 El Camino Real, Palo Alto, CA 94301",
    },
    {
        "contact_id": "cnt_002",
        "full_name": "Brian Kowalski",
        "email": "b.kowalski@enterprise.io",
        "personal_email": "briankowalski77@yahoo.com",
        "mobile": "312-555-8814",
        "direct_line": "(312) 555-2200",
        "ssn": "442-19-7730",
        "home_address": "88 N Michigan Ave, Chicago, IL 60611",
    },
    {
        "contact_id": "cnt_003",
        "full_name": "Yuki Tanaka",
        "email": "y.tanaka@globalfirm.co",
        "personal_email": "yukitanaka1990@icloud.com",
        "mobile": "415-555-6609",
        "home_address": "307 Market St, San Francisco, CA 94102",
    },
]


def get_contact(contact_id: str) -> dict | None:
    return next((c for c in CONTACTS if c["contact_id"] == contact_id), None)


def search_by_email(email: str) -> dict | None:
    return next(
        (c for c in CONTACTS if c.get("email") == email or c.get("personal_email") == email),
        None,
    )
