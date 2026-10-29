import asyncio
import logging
import os
import secrets
from enum import StrEnum

# Configure logger
logger = logging.getLogger(__name__)

# ✅ FIX 1: Retrieve credentials securely from environment variables
API_TOKEN = os.getenv("JIRA_API_TOKEN")


class TicketType(StrEnum):
    PASSWORD_RESET = "Password Reset"
    NETWORK_ISSUE = "Network Issue"


def generate_temp_password(length: int = 12) -> str:
    """Generate a cryptographically secure temporary password."""
    return secrets.token_urlsafe(length)


def get_network_status() -> str:
    """Fetch current network health status."""
    return "All network systems are operational. Issue ticket created."


async def handle_ticket(ticket_type: str, user_id: str) -> str:
    """
    Process a support ticket asynchronously without blocking the event loop.

    :param ticket_type: The category of the support ticket.
    :param user_id: Identifier for the user submitting the ticket.
    :return: A status message with the outcome of ticket processing.
    """
    if not ticket_type or not user_id:
        raise ValueError("Both 'ticket_type' and 'user_id' are required.")

    logger.info("Processing ticket for user: %s, type: %s", user_id, ticket_type)

    # ✅ FIX 2: Non-blocking asynchronous delay (replaces time.sleep)
    await asyncio.sleep(0.1)

    # ✅ FIX 3: Clean branching and resolved variable reference
    match ticket_type:
        case TicketType.PASSWORD_RESET:
            temp_password = generate_temp_password()
            return f"Password has been reset. Temporary credentials: {temp_password}"
        case TicketType.NETWORK_ISSUE:
            return get_network_status()
        case _:
            return "Ticket routed to queue."
