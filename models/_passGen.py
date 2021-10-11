from hashlib import sha512


def generate_password(password: str) -> str:
    """
    Generates a password hash using sha512
    """
    return sha512(password.encode('utf-8')).hexdigest()
