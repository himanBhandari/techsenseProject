# password_utils.py

import hashlib
import re

def get_password_hash(password: str) -> str:
    """
    Converts a password to its SHA-1 hash.
    """
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1_hash

def validate_password_strength(password: str) -> bool:
    """
    Validates if a password is strong enough.
    """
    if len(password) < 8:
        print("Password should be at least 8 characters long.")
        return False
    if not re.search(r'[A-Z]', password):
        print("Password should contain at least one uppercase letter.")
        return False
    if not re.search(r'[a-z]', password):
        print("Password should contain at least one lowercase letter.")
        return False
    if not re.search(r'[0-9]', password):
        print("Password should contain at least one digit.")
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("Password should contain at least one special character.")
        return False
    return True

def contains_common_pattern(password: str) -> bool:
    """
    Checks if the password contains common patterns like '1234', 'password', etc.
    """
    common_patterns = ['1234', 'password', 'qwerty', 'abc123', 'letmein']
    for pattern in common_patterns:
        if pattern in password.lower():
            print(f"Password contains a common pattern: {pattern}.")
            return True
    return False

def check_for_dictionary_words(password: str) -> bool:
    """
    Checks if the password contains any dictionary words.
    """
    dictionary_words = ["password", "admin", "welcome", "user", "123456"]
    for word in dictionary_words:
        if word in password.lower():
            print(f"Password contains a dictionary word: {word}.")
            return True
    return False