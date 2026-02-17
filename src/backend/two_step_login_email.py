"""
Functions in this file are responsible for working with OTP codes.
"""

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
    """
    This function is responsible for sending emails contain one time passwords for registration.
    :param email: user email.
    :param otp_code: one time password.
    :return: nothing, only sends emails.
    """
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
    """
    This function is responsible for generating one time passwords.
    :param secret: secret for password.
    :return: one time password.
    """
    totp = TOTP(secret)
    return totp.now()


def two_step_login(user_email: str) -> Tuple[bool, Any]:
    """
    This function is responsible for generate otp and send it via email.
    :param user_email: user email.
    :return: success.
    """
    try:
        secret = "JBSWY3DPEHPK3PXP"
        otp_code = generate_otp(secret)
        send_otp_via_email(user_email, otp_code)
        return True, otp_code
    except Exception as error:
        print(f"Error: {error}")
        return False, 0
