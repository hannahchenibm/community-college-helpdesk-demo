import logging
import os

logger = logging.getLogger(__name__)

# Loaded from the environment (or a secrets vault); never hardcode or commit it.
# Not read at import time so the module can be imported without the secret set.
def get_api_token() -> str:
    token = os.environ.get("JIRA_SERVICE_TOKEN")
    if not token:
        raise RuntimeError("JIRA_SERVICE_TOKEN is not configured")
    return token


PASSWORD_RESET = "Password Reset"
NETWORK_ISSUE = "Network Issue"

RESPONSES = {
    PASSWORD_RESET: "Password reset instructions have been sent to your registered email.",
    NETWORK_ISSUE: "Network issue ticket routed to the network team.",
}
DEFAULT_RESPONSE = "Ticket routed to queue."


def handle_ticket(ticket_type: str, user_id: str) -> str:
    """Return the user-facing response for a help desk ticket."""
    if not isinstance(ticket_type, str) or not isinstance(user_id, str) or not user_id.strip():
        raise ValueError("Invalid ticket request")

    logger.info("Processing ticket", extra={"user_id": user_id, "ticket_type": ticket_type})
    return RESPONSES.get(ticket_type, DEFAULT_RESPONSE)
