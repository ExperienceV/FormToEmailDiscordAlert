# Welcome, User!

This application is designed to handle "Contact Us" forms. It manages the sending of emails and notifies a Discord channel whenever there is a new contact message.

## How the Application Works
1. **Email Handling**: When a user submits a contact form, the application sends the form data via email to a specified recipient.
2. **Discord Notification**: A notification is sent to a specified Discord channel to alert the team about new contact messages.

## Prerequisites
To ensure the proper functioning of the application, you will need to configure the following data:

1. **Resend API Key**: This key allows the application to send emails using the Resend API.
2. **Discord Role ID**: The ID of the role in Discord that will be mentioned in the notification.
3. **Webhook URL (WH_URL)**: Integrate a Discord webhook into a channel and obtain its URL for notifications.
4. **Sender Email (SENDER_MAIL)**: The email address used to send contact form data. It should be the one provided by Resend. If you wish to use a custom email, you’ll need to configure a custom domain with Resend.
5. **Receiver Email (RECEIVER_MAIL)**: The email address where all the contact form submissions will be delivered.

## Setup Instructions

To configure these parameters, create an .env file in the api directory `api/.env` 
and add the required information

The `.env` file should look like this:

```env
RESEND_KEY=your_resend_api_key
ROLE_ID=your_discord_role_id
WH_URL=your_discord_webhook_url
SENDER_MAIL=your_sender_email
RECEIVER_MAIL=your_receiver_email
