import requests
import os

def send_discord_msg() -> bool:
    """
    Sends a notification message to a Discord channel using a webhook URL.

    The function retrieves the role ID and webhook URL from environment variables,
    constructs a JSON payload, and sends it to the specified webhook. The message
    tags the specified role to notify them about a new job offer.

    Returns:
        bool: True if the message was sent successfully, False otherwise.
    """
    # Retrieve the role ID from environment variables
    role_id = os.getenv('ROLE_ID')
    if not role_id:
        raise ValueError("ROLE_ID environment variable is not set")

    # Construct the message payload
    data = {
        'content': f'<@&{role_id}> A job offer has arrived, take a look at it!'
    }

    # Retrieve the webhook URL from environment variables
    wh = os.getenv('WH_URL')
    if not wh:
        raise ValueError("WH_URL environment variable is not set")

    # Send the message to the Discord webhook
    response = requests.post(wh, json=data)

    # Check the response status code
    if response.status_code == 204:
        # Message sent successfully
        return True
    else:
        # Log or handle the failure as needed
        return False
