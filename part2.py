import hashlib
import random
import string

PASSWORD = "comp2108"
HASH = "9f02b0fd48e9211a5a33ae3321b942896e4ebb0cb267fdfff53fa58cf8c56f24"

def increment_salt(salt: list[str]):
    """Increment the salt in a sequential manner"""
    for i in range(7, -1, -1):
        if salt[i] != 'z':
            salt[i] = chr(ord(salt[i]) + 1)

        salt[i] = 'a'

def find_salt() -> str:
    """
    Return the salt that returns the provided HASH for password
    'comp2108'
    """
    salt_lst = ['a'] * 8
    while True:
        salt = "".join(salt_lst)
        password = PASSWORD + salt
        hash = hashlib.sha256(password.encode()).hexdigest()
        if hash == HASH:
            return salt
        
        increment_salt(salt_lst)
        
print(find_salt())