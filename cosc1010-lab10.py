# Braeden Kirby
# UWYO COSC 1010
# 11/21/2024
# Lab 10
# Lab Section: 13
# Sources, people worked with, help given to: Matthew Curl
# your
# comments
# here

#import modules you will need 

from hashlib import sha256
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()



# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.

# I can set the file path and rockyou path using the path function

file_path = Path('hash')

rockyou_path = Path('rockyou.txt')

# - Read in the value stored within `hash`.
#   - You must use a try and except block.

# I will use a try and except statment to open the fuile path and set the hash password variable 

try:

    hash_file = file_path.open('r')

    hash_password = hash_file.read().strip()

# This except will cover all of the except errors instead of doing a FileNotFound exception

except:

    print('File was not found')

# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.

# I can complete the task above using the open method on the rockyou path 

try:

    rockyou_file = rockyou_path.open('r')

    possible_passwords = rockyou_file.readlines()

except:

    print('The necessary file was not found')

# I can use a for loop to use the get function and find the password then print out the password if the found password is correct

for password in possible_passwords:

    password = password.strip()

    hashed_password = get_hash(password)

    if hashed_password == hash_password:

        print(f'The Password was: {password}')

        break