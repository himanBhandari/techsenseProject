from password_utils import (
    get_password_hash,
    validate_password_strength,
    contains_common_pattern,
    check_for_dictionary_words
)
from pwned_api import check_password_breach


def check_password(password: str):
    """
    Checks a single password for breaches.
    Returns a result string.
    """

    # Step 1: Validate password strength
    if not validate_password_strength(password):
        return "❌ Password is weak. Please choose a stronger password."

    # Step 2: Check for common patterns or dictionary words
    if contains_common_pattern(password) or check_for_dictionary_words(password):
        return "❌ Password is weak due to common patterns or dictionary words."

    # Step 3: Get SHA-1 hash
    sha1_hash = get_password_hash(password)

    # Step 4: Split hash
    hash_prefix = sha1_hash[:5]
    hash_suffix = sha1_hash[5:]

    # Step 5: Check breach database
    breach_found = check_password_breach(hash_prefix, hash_suffix)

    if breach_found:
        return "⚠️ This password has appeared in data breaches."

    return "✅ Your password has not been found in known breaches."


def check_multiple_passwords(passwords: list):
    """
    Checks a list of passwords for breaches.
    Returns a list of results.
    """

    results = []

    for password in passwords:
        result = check_password(password)
        results.append(f"{password} → {result}")

    return results