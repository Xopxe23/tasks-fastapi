from email.message import EmailMessage

from pydantic import EmailStr

from config import settings


def create_email_verification_template(
        email_to: EmailStr,
        token: str
) -> EmailMessage:
    email = EmailMessage()
    email["Subject"] = "Email Verification"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to
    email.set_content(
        f'''
            <h1>Verify your email</h1>
            <p>You're registered on Task APP! Verify your email please.</p>
            <p>Please ENTER your TOKEN:</p>
            <h5>{token}</h5>
        ''',
        subtype="html"
    )
    return email
