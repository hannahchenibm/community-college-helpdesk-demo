import logging
import os

logger = logging.getLogger(__name__)

PASSWORD_RESET = "Password Reset"
NETWORK_ISSUE = "Network Issue"


def get_api_token() -> str:
    """Read the Jira service token from the environment (never hardcode secrets)."""
    token = os.environ.get("JIRA_SERVICE_TOKEN")
    if not token:
        raise RuntimeError("JIRA_SERVICE_TOKEN environment variable is not set")
    return token


def handle_ticket(ticket_type: str, user_id: str) -> str:
    """Route a helpdesk ticket and return a user-facing status message."""
    if not all(isinstance(v, str) and v.strip() for v in (ticket_type, user_id)):
        raise ValueError("ticket_type and user_id must be non-empty strings")

    logger.info("Processing ticket", extra={"ticket_type": ticket_type, "user_id": user_id})

    if ticket_type == PASSWORD_RESET:
        # Never return or log a plaintext password; send a one-time reset link instead.
        return "A password reset link has been sent to your registered email."
    if ticket_type == NETWORK_ISSUE:
        return "Network issue logged. A network engineer will contact you shortly."
    return "Ticket routed to queue."
