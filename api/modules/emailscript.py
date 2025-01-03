import resend
import os

def resend_mail(message, issue, client_mail, username):
    """
    Function that sends an email using the Resend API.
    
    This function formats the provided message and sends it via email, 
    including information such as the user's name, email, and the issue.
    
    Args:
        message (str): The content of the message to be sent.
        issue (str): The subject of the email.
        client_mail (str): The email address of the client.
        username (str): The username of the client sending the message.
    
    Returns:
        resend.Emails.SendResponse: The response object from the Resend API containing email details.
    
    Raises:
        Exception: If there is an error while sending the email, it will be caught and printed.
    """
    try:
        # Set the Resend API key from the environment variables
        resend.api_key = os.getenv('RESEND_KEY')

        # Format the message with the user's details
        ident_message = dot_separator(message)
        build_message = f"User: @{username}\nEmail: {client_mail}\nMessage: {ident_message}"

        # Prepare the email parameters
        params: resend.Emails.SendParams = {
            "from": os.getenv('SENDER_MAIL'),
            "to": os.getenv('RECEIVER_MAIL'),
            "subject": issue,
            "text": build_message
        }

        # Send the email using Resend API and return the response
        email = resend.Emails.send(params)
        return email
    except Exception as e:
        # Print any errors that occur during email sending
        print(e)


def dot_separator(text):
    """
    Function that formats a message by replacing '. ' with a newline.
    
    This is useful for separating different parts of the message to 
    make it more readable when sent via email.
    
    Args:
        text (str): The text message to be formatted.
    
    Returns:
        str: The formatted message with line breaks where appropriate.
    """
    # Replace '. ' with '.\n' to separate sentences
    modify_text = text.replace('. ', '.\n')
    
    # Ensure the message ends with a newline if it ends with a period
    if modify_text.endswith('.'):
        modify_text += '\n'
    
    return modify_text
