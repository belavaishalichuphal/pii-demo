"""
User service module - no personally identifiable information stored here.
All user data is referenced by opaque IDs only.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    user_id: str
    role: str
    is_active: bool
    department_code: str
    created_at: str


def get_user(user_id: str) -> Optional[User]:
    """Fetch a user by their internal ID."""
    # ID lookup only — no PII in this layer
    return None


def list_active_users() -> list[User]:
    """Return all active users (IDs and roles only)."""
    return []


def deactivate_user(user_id: str) -> bool:
    """Deactivate a user account by ID."""
    return True
