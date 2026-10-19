import os
import asyncio
import logging

logger = logging.getLogger(__name__)

# ✅ FIX 1: Load secret from environment variable — never hardcode credentials
API_TOKEN = os.environ.get("JIRA_API_TOKEN")

async def handle_ticket(ticket_type: str, user_id: str) -> str:
    """Process a helpdesk ticket asynchronously.

    Args:
        ticket_type: Category of the ticket (e.g. "Password Reset").
        user_id: Identifier of the requesting user.

    Returns:
        A string describing the outcome.
    """
    logger.info("Processing ticket for user %s", user_id)

    # ✅ FIX 2: Non-blocking async sleep — frees the event loop while waiting
    await asyncio.sleep(5)

    if ticket_type == "Password Reset":
        return "Password has been reset. A temporary password has been sent to your registered email."
    elif ticket_type == "Network Issue":
        # ✅ FIX 3: Return a real value instead of an undefined variable
        return "Network issue logged. Our team will investigate and contact you shortly."
    else:
        return "Ticket routed to queue."