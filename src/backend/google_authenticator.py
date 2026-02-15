import time

import pyotp
import qrcode


def create_qr_code(username: str) -> str:
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    uri = totp.provisioning_uri(f"{username}", issuer_name="Smart Advisor MT5")

    qr = qrcode.make(uri)
    qr_file = "src\\assets\\google_authenticator_qr.png"
    qr.save(qr_file)
    time.sleep(1)
    return secret


def verify_qr_code(user_code: str, secret: str) -> bool:
    totp = pyotp.TOTP(secret)

    if totp.verify(user_code):
        return True
    else:
        return False
