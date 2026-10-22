import asyncio
import logging
import os

logger = logging.getLogger(__name__)

# ✅ FIX 1: Load secret from environment — never hardcode credentials
API_TOKEN = os.environ.get("JIRA_API_TOKEN")


async def handle_ticket(ticket_type: str, user_id: str) -> str:
    """Process a helpdesk ticket asynchronously."""
    logger.info("Processing ticket for user %s", user_id)

    # ✅ FIX 2: Non-blocking async sleep — releases the event loop during the wait
    await asyncio.sleep(5)

    if ticket_type == "Password Reset":
        return "Password has been reset. Please check your email for the temporary password."
    elif ticket_type == "Network Issue":
        # ✅ FIX 3: Return a real status string instead of an undefined variable
        return "Network issue logged. Our team is investigating."
    else:
        return "Ticket routed to queue."
