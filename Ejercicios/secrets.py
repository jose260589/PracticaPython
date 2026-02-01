import secrets

def generate_otp(length=6):
    """Generates a secure one-time password (OTP) of specified length."""
    return ''.join(str(secrets.randbelow(10)) for _ in range(length))

print("Generated OTP:", generate_otp())

#source code --clcoding.comn