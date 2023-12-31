import smtplib

from pydantic import EmailStr

from src.config import settings
from src.tasks.celery import celery
from src.tasks.email_temolates import create_email_verification_template


@celery.task
def sent_verification_email(
    email_to: EmailStr,
    token: str
):
    email_to = email_to
    msg_content = create_email_verification_template(email_to, token)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)
    return f'Token {token} has been sent successfully on {email_to}'
