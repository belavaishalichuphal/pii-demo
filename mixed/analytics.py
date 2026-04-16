"""
Analytics module — mostly clean, but some debug statements contain PII.
WARNING: This file has partial PII violations in debug/logging paths.
"""

import logging

logger = logging.getLogger(__name__)

# Clean: aggregated metrics only
MONTHLY_STATS = {
    "signups": 1482,
    "churned": 93,
    "mrr_usd": 48200,
    "avg_session_minutes": 14.3,
}


def get_monthly_summary() -> dict:
    """Return aggregated monthly metrics. No PII."""
    return MONTHLY_STATS


def compute_retention_rate() -> float:
    """Compute monthly retention rate from aggregate data."""
    churned = MONTHLY_STATS["churned"]
    total = MONTHLY_STATS["signups"]
    return round((total - churned) / total * 100, 2)


# VIOLATION: debug log accidentally includes PII from a real support case
def debug_failed_payment(order_id: str) -> None:
    """Temporary debug helper — should never reach production."""
    logger.debug(
        "Payment failed for order %s — customer: Jennifer Walsh, "
        "email: j.walsh@gmail.com, card: 4532-1188-2234-9901, CVV: 312",
        order_id,
    )


# Clean: event tracking by user_id only
def track_event(user_id: str, event: str, properties: dict) -> None:
    """Track a product event. Uses opaque user_id — no PII."""
    logger.info("event=%s user_id=%s props=%s", event, user_id, properties)
