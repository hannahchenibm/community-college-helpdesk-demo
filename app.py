import asyncio
import os

API_TOKEN = os.environ.get("JIRA_SERVICE_TOKEN")

async def handle_ticket(ticket_type: str, user_id: str) -> str:
    print(f"Processing ticket for user {user_id}...")

    await asyncio.sleep(5)

    if ticket_type == "Password Reset":
        return "Password has been reset. Please check your email for the temporary password."
    elif ticket_type == "Network Issue":
        return "Network issue reported. Our team is investigating."
    else:
        return "Ticket routed to queue."
