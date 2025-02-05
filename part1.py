import hashlib
import random
import string

STUDENT_NUMBER = "101230436"
LAST_TWO_DIGITS = STUDENT_NUMBER[-2:]

def random_password() -> str:
    """
    Returns random password of length 8
    consisting of lowercase letters and numbers
    """
    chars = string.ascii_lowercase + string.digits
    result = "".join(random.choices(chars, k=8))
    return result

def find_hash() -> str:
    """
    Return password and hash that starts with 'cOffee' followed
    by last 2 digits of my student number (36)
    """
    while True:
        password = random_password()
        combined = password + STUDENT_NUMBER
        hash = hashlib.sha256(combined.encode()).hexdigest()
        if(hash.startwith(f"c0ffee{LAST_TWO_DIGITS}")):
            return password, hash

if __name__ == "__main__":
    password = find_hash()
    with open("file1.txt", "w") as file:
        file.write(password)