import asyncio
import logging
import os

logger = logging.getLogger(__name__)

# Loaded from the environment (never hardcode secrets). Set JIRA_SERVICE_TOKEN
# via your shell, a secrets manager, or an untracked .env file.
API_TOKEN = os.environ.get("JIRA_SERVICE_TOKEN")

PASSWORD_RESET = "Password Reset"
NETWORK_ISSUE = "Network Issue"


async def handle_ticket(ticket_type: str, user_id: str) -> str:
    """Process a helpdesk ticket and return a user-facing status message."""
    logger.info("Processing ticket", extra={"user_id": user_id, "ticket_type": ticket_type})

    # Non-blocking simulated work: yields to the event loop instead of
    # freezing the worker for 5 seconds on every request.
    await asyncio.sleep(5)

    if ticket_type == PASSWORD_RESET:
        # Never return or log a plaintext password. Deliver a single-use reset
        # link out-of-band (e.g. email) instead.
        return "A password reset link has been sent to your registered email."
    if ticket_type == NETWORK_ISSUE:
        return "Network issue logged. Our team is investigating."
    return "Ticket routed to queue."
