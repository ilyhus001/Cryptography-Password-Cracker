import hashlib
import sys

PASSWORD = "comp2108"
HASH = "9f02b0fd48e9211a5a33ae3321b942896e4ebb0cb267fdfff53fa58cf8c56f24"

def increment_salt(salt: list[str]):
    """Increment the salt in a sequential manner"""
    for i in range(6, -1, -1):
        if salt[i] != 'z':
            salt[i] = chr(ord(salt[i]) + 1)
            return salt
        else:
            salt[i] = 'a'
    return salt        

def find_salt(letter) -> str:
    """
    Return the salt that returns the provided HASH for password
    'comp2108'
    """
    salt_lst = [letter] + ['a'] * 7 
    salt = "".join(salt_lst)
    while True:
        password = PASSWORD + salt
        hash = hashlib.sha256(password.encode()).hexdigest()
        if hash == HASH:
            return salt
        
        salt_lst = increment_salt(salt_lst)
        salt = "".join(salt_lst)
    

if __name__ == "__main__":
   salt = find_salt(sys.argv[1])
   with open("part2.txt", "w") as file:
       file.write(salt)

    

       