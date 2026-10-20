import logging
import os

logger = logging.getLogger(__name__)

PASSWORD_RESET = "Password Reset"
NETWORK_ISSUE = "Network Issue"


def get_api_token() -> str:
    """Read the Jira service token from the environment (never hardcode it)."""
    token = os.environ.get("JIRA_API_TOKEN")
    if not token:
        raise RuntimeError("JIRA_API_TOKEN environment variable is not set")
    return token


def handle_ticket(ticket_type: str, user_id: str) -> str:
    """Route a helpdesk ticket and return a user-facing status message."""
    if not isinstance(user_id, str) or not user_id.strip():
        raise ValueError("user_id must be a non-empty string")

    logger.info("Processing ticket", extra={"user_id": user_id, "ticket_type": ticket_type})

    if ticket_type == PASSWORD_RESET:
        # Never return or log a password; deliver a single-use reset link out of band.
        return "A password reset link has been sent to your registered email address."
    if ticket_type == NETWORK_ISSUE:
        return "Network issue logged. A network engineer will follow up shortly."
    return "Ticket routed to queue."
