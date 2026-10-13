import asyncio
import logging
import os

# ✅ FIX 1: Load secret from environment — never hardcode credentials.
# Set the JIRA_API_TOKEN environment variable before running this service.
API_TOKEN = os.environ.get("JIRA_API_TOKEN")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


# ✅ FIX 2: Async function — non-blocking; the event loop can handle other
# requests while this coroutine awaits, preventing thread starvation.
async def handle_ticket(ticket_type: str, user_id: str) -> str:
    logger.info("Processing ticket", extra={"user_id": user_id, "ticket_type": ticket_type})

    await asyncio.sleep(5)  # non-blocking delay

    if ticket_type == "Password Reset":
        # ✅ FIX 4: Never return a hardcoded temporary password in a response.
        return "Password reset initiated. Instructions have been sent to the user's registered email."
    elif ticket_type == "Network Issue":
        # ✅ FIX 3: Return a defined value instead of a bare undefined name.
        return "Network issue logged. The infrastructure team has been notified."
    else:
        return "Ticket routed to queue."