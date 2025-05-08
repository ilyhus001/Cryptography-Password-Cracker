from os import urandom
from base64 import b64encode
import string

def random_salts() -> set[str]:
    """
    Generate 16 random salts and return a list
    containing these salts. Each salt is composed
    of ASCII digits and lowercase characters. Each 
    salt is pairwise distinct from other salts.
    """
    chars = string.digits + string.ascii_lowercase
    salts = set()

    while len(salts) < 16:
        bytes = urandom(500)
        salt = b64encode(bytes).decode('ASCII')
        salts.add("".join(char for char in salt if char in chars)[:16])

    return salts


if __name__ == "__main__":
    salts = random_salts()
    for salt in salts:
        with open("part3.txt", "a") as file:
            file.write(salt+"\n")