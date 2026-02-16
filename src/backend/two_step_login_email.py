import os
from pathlib import Path
from typing import Tuple, Any

from dotenv import load_dotenv
from smtplib import SMTP_SSL
from pyotp import TOTP
from email.message import EmailMessage

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)


def send_otp_via_email(email: str, otp_code: str) -> None:
    sender_email = os.getenv("GMAIL_EMAIL")
    sender_password = os.getenv("OTP_GMAIL_PASSWORD")
    subject = "Smart Advisor MT5 e-mail verification code"

    msg = EmailMessage()
    msg.set_content(f"Your verification code: {otp_code}")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = email

    with SMTP_SSL("smtp.gmail.com", 465) as serv:
        serv.login(sender_email, sender_password)
        serv.send_message(msg)


def generate_otp(secret: str) -> str:
    totp = TOTP(secret)
    return totp.now()


def two_step_login(user_email: str) -> Tuple[bool, Any]:
    try:
        secret = os.getenv("SECRET")
        otp_code = generate_otp(secret)
        send_otp_via_email(user_email, otp_code)
        return True, otp_code
    except Exception as error:
        print(f"Error: {error}")
        return False, 0
