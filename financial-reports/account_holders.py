"""
Account holder records for financial reporting.
WARNING: Contains PII including bank account details and SSNs.
This file should be flagged by PII and financial data compliance checks.
"""

# Account holder records with sensitive financial PII
ACCOUNT_HOLDERS = [
    {
        "account_id": "ACC-8801",
        "full_name": "Diane Holloway",
        "email": "diane.holloway@gmail.com",
        "phone": "314-555-6612",
        "ssn": "482-39-7701",
        "dob": "1971-10-04",
        "address": "220 S Grand Blvd, St. Louis, MO 63103",
        "bank_account": "071000013-442219930",  # routing-account
        "aba_routing": "071000013",
        "account_number": "442219930",
        "account_type": "checking",
        "balance_usd": 14820.44,
    },
    {
        "account_id": "ACC-8802",
        "full_name": "Raymond Cho",
        "email": "raymond.cho@hotmail.com",
        "phone": "(323) 555-4480",
        "ssn": "305-72-6619",
        "dob": "1984-02-17",
        "address": "4400 Wilshire Blvd, Los Angeles, CA 90010",
        "bank_account": "322271627-891004412",
        "aba_routing": "322271627",
        "account_number": "891004412",
        "account_type": "savings",
        "balance_usd": 32190.00,
    },
    {
        "account_id": "ACC-8803",
        "full_name": "Natalie Brennan",
        "email": "n.brennan@icloud.com",
        "phone": "617-555-0099",
        "ssn": "219-88-5530",
        "dob": "1990-07-30",
        "address": "1 Federal St, Boston, MA 02110",
        "bank_account": "011000138-772013489",
        "aba_routing": "011000138",
        "account_number": "772013489",
        "account_type": "checking",
        "balance_usd": 8440.12,
    },
]


def get_account(account_id: str) -> dict | None:
    return next((a for a in ACCOUNT_HOLDERS if a["account_id"] == account_id), None)


def lookup_by_ssn(ssn: str) -> dict | None:
    """Highly sensitive — SSN-based account lookup."""
    return next((a for a in ACCOUNT_HOLDERS if a.get("ssn") == ssn), None)
