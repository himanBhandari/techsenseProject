# check_breach.py

from password_utils import get_password_hash, validate_password_strength, contains_common_pattern, check_for_dictionary_words
from pwned_api import check_password_breach

def check_password(password: str):
    """
    Checks a single password for breaches.
    """
    # Step 1: Validate password strength
    if not validate_password_strength(password):
        print("Password is weak. Please choose a stronger password.")
        return

    # Step 2: Check for common patterns or dictionary words
    if contains_common_pattern(password) or check_for_dictionary_words(password):
        print("Password is weak due to common patterns or dictionary words.")
        return

    # Step 3: Get the SHA-1 hash of the password
    sha1_hash = get_password_hash(password)

    # Step 4: Get the first 5 characters (prefix) and the rest of the hash (suffix)
    hash_prefix = sha1_hash[:5]
    hash_suffix = sha1_hash[5:]

    # Step 5: Check if the password has been breached using the API
    breach_found = check_password_breach(hash_prefix, hash_suffix)

    if not breach_found:
        print("Your password has not been found in any breaches.")

def check_multiple_passwords(passwords: list):
    """
    Checks a list of passwords for breaches.
    """
    print("Checking multiple passwords...\n")
    for password in passwords:
        print(f"Checking password: {password}")
        check_password(password)
        print("-" * 50)  # Separator for readability