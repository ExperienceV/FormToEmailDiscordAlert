from fastapi import APIRouter, HTTPException, status
from fastapi.responses import HTMLResponse
from api.modules.webhook import send_discord_msg
from api.modules.emailscript import resend_mail
from api.models import form_model

# Create an instance of FastAPI's APIRouter
app = APIRouter()

@app.get("/")
async def index_text():
    """
    Endpoint that responds with a simple greeting message.
    
    Returns:
        dict: A message with a FastAPI greeting.
    """
    return {"message": "Hello from FastAPI!"}

@app.post("/send_email", response_class=HTMLResponse)
async def send_email(form: form_model):
    """
    Endpoint that processes sending an email and a Discord notification.
    
    Validates the provided form data and performs two operations:
    1. Attempts to send an email using the `resend_mail` function.
    2. If the email sending is successful, attempts to send a message to Discord using `send_discord_msg`.
    
    Args:
        form (form_model): The submitted form data, which includes the user's name, email, subject, and message.
    
    Raises:
        HTTPException: If any operation (email sending or Discord notification) fails, an HTTP exception is raised with the corresponding status code.
    
    Returns:
        HTTPException: If both operations succeed, a response with status code 200 (OK) is returned.
    """
    
    # Attempt to send the email using the form data
    response = resend_mail(
        username=form.name,
        client_mail=form.mail,
        issue=form.issue,
        message=form.message
    )

    # If email sending fails, raise an HTTPException with status 405
    if not response:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail='Ooops, mail sending failed'
        )

    # Attempt to send a Discord message
    discord_request = send_discord_msg()

    # If Discord message sending fails, raise an HTTPException with status 405
    if not discord_request:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail='Discord webhook failed'
        )

    # If both operations succeed, return a success message with status 200
    raise HTTPException(
        status_code=status.HTTP_200_OK,
        detail='Everything is fine.'
    )
