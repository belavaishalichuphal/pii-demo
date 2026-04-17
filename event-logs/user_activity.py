"""
User activity event log snapshot.
WARNING: Several log entries below accidentally captured PII in free-text fields.
"""

import json
from datetime import datetime

# Raw event log entries — some contain PII in message/metadata fields
EVENT_LOG = [
    {
        "event_id": "evt_10091",
        "timestamp": "2026-03-15T10:22:14Z",
        "event_type": "user.login",
        "user_id": "usr_4412",
        "ip": "192.0.2.55",
        "user_agent": "Mozilla/5.0",
        "status": "success",
        # Clean — no PII beyond opaque user_id
    },
    {
        "event_id": "evt_10092",
        "timestamp": "2026-03-15T10:23:01Z",
        "event_type": "support.chat_opened",
        "user_id": "usr_8830",
        "message": "Hi, I'm Patricia Huang, email patricia.h@gmail.com, phone 646-555-9902. I need help with my account.",
        # VIOLATION: full name, email, phone in freetext message
    },
    {
        "event_id": "evt_10093",
        "timestamp": "2026-03-15T10:25:44Z",
        "event_type": "payment.failed",
        "user_id": "usr_2291",
        "error_code": "card_declined",
        "status": "failed",
        # Clean — no PII
    },
    {
        "event_id": "evt_10094",
        "timestamp": "2026-03-15T10:31:09Z",
        "event_type": "account.password_reset",
        "user_id": "usr_5512",
        "debug_note": "Reset initiated for George Albright, dob 1975-08-19, SSN 302-44-7821, address: 330 Park Ave, NY 10022",
        # VIOLATION: name, DOB, SSN, address in debug field
    },
    {
        "event_id": "evt_10095",
        "timestamp": "2026-03-15T10:45:00Z",
        "event_type": "export.completed",
        "user_id": "usr_7701",
        "export_id": "exp_20260315_009",
        "rows_exported": 1204,
        # Clean — no PII
    },
]


def get_events_by_type(event_type: str) -> list[dict]:
    return [e for e in EVENT_LOG if e["event_type"] == event_type]


def dump_log() -> str:
    return json.dumps(EVENT_LOG, indent=2)
