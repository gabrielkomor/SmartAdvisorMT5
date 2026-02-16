"""
This file is responsible for generating and verifying the QR code used in the user account creation process.
"""

import time

import pyotp
import qrcode


def create_qr_code(username: str) -> str:
    """
    This function is responsible for generating qr code needed in login process.
    :param username: username.
    :return: creates temporary qr code and secret.
    """
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    uri = totp.provisioning_uri(f"{username}", issuer_name="Smart Advisor MT5")

    qr = qrcode.make(uri)
    qr_file = "src\\assets\\google_authenticator_qr.png"
    qr.save(qr_file)
    time.sleep(1)
    return secret


def verify_qr_code(user_code: str, secret: str) -> bool:
    """
    This function is responsible for verify qr code correctness.
    :param user_code: user code.
    :param secret: secret.
    :return: boolean.
    """
    totp = pyotp.TOTP(secret)

    if totp.verify(user_code):
        return True
    else:
        return False
