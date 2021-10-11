from hashlib import sha512
import random


def ID_generator(i_type: str, name: str) -> str:
    """
    Generates an ID for a user based on their email address.

    """
    return i_type + sha512(name.encode() + str(random.randint(0, 9999999999)).encode()).hexdigest()
