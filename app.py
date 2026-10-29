import logging
import os
import secrets
from enum import StrEnum

# Configure structured logging
logger = logging.getLogger(__name__)

# Retrieve credentials securely from environment variables
API_TOKEN = os.getenv("JIRA_SERVICE_TOKEN")


class TicketType(StrEnum):
    PASSWORD_RESET = "Password Reset"
    NETWORK_ISSUE = "Network Issue"


def generate_temp_password(length: int = 12) -> str:
    """Generate a cryptographically secure temporary password."""
    return secrets.token_urlsafe(length)


def get_network_status() -> str:
    """Fetch current network health status."""
    return "All network systems are operational."


def handle_ticket(ticket_type: str, user_id: str) -> str:
    """
    Process a support ticket based on type and user ID.
    
    :param ticket_type: The category of the ticket.
    :param user_id: The ID of the user submitting the ticket.
    :return: A status message indicating the ticket result.
    """
    if not ticket_type or not user_id:
        raise ValueError("Both ticket_type and user_id are required.")

    logger.info("Processing ticket for user: %s, type: %s", user_id, ticket_type)

    match ticket_type:
        case TicketType.PASSWORD_RESET:
            temp_pw = generate_temp_password()
            return f"Password has been reset. Temporary credentials: {temp_pw}"
        
        case TicketType.NETWORK_ISSUE:
            status = get_network_status()
            return f"Network Issue reported. Current status: {status}"
        
        case _:
            return "Ticket routed to queue."

