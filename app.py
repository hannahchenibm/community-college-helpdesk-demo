import asyncio
import logging
import os

# ✅ FIX 1: Load secret from environment variable, never hardcode credentials
API_TOKEN = os.environ.get("JIRA_SERVICE_TOKEN")

logger = logging.getLogger(__name__)

async def handle_ticket(ticket_type: str, user_id: str) -> str:
    """Process a helpdesk ticket asynchronously.

    Args:
        ticket_type: The category of the ticket (e.g. "Password Reset").
        user_id: The identifier of the requesting user.

    Returns:
        A status message string.
    """
    logger.info("Processing ticket for user %s", user_id)

    # ✅ FIX 2: Non-blocking async sleep — does not stall the event loop
    await asyncio.sleep(5)

    if ticket_type == "Password Reset":
        # Trigger a secure reset flow rather than returning a plaintext password
        return "Password reset email sent. Please check your inbox."
    elif ticket_type == "Network Issue":
        # ✅ FIX 3: Use a defined variable instead of a non-existent one
        network_status = "degraded" if not _is_network_healthy() else "operational"
        return f"Network status: {network_status}. Ticket logged for review."
    else:
        return "Ticket routed to queue."


def _is_network_healthy() -> bool:
    """Return True if the network is reachable. Stub for integration."""
    return True
