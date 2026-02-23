# pwned_api.py

import requests
import time
import hashlib

# Cache to avoid querying the same hash prefix repeatedly
cache = {}

def query_pwned_api(hash_prefix: str) -> str:
    """
    Queries the Have I Been Pwned API to check for known breaches for a given hash prefix.
    """
    if hash_prefix in cache:
        print(f"Using cached data for hash prefix {hash_prefix}.")
        return cache[hash_prefix]
    
    url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
    
    retries = 3
    for _ in range(retries):
        try:
            response = requests.get(url)

            # Check for successful response
            if response.status_code == 200:
                cache[hash_prefix] = response.text
                return response.text
            else:
                print(f"Error: Unable to check password breach status. Status Code: {response.status_code}")
                return ""
        
        except requests.RequestException as e:
            print(f"Error occurred while fetching data: {e}")
            time.sleep(2)  # Wait before retrying

    print(f"Failed to retrieve data for hash prefix {hash_prefix} after {retries} attempts.")
    return ""

def check_password_breach(hash_prefix: str, hash_suffix: str) -> bool:
    """
    Checks if the password (using its hash suffix) has been pwned.
    """
    # Get the list of breached hashes from the API response
    response_text = query_pwned_api(hash_prefix)

    if not response_text:
        return False

    # Check each line of the response to find the hash suffix
    for entry in response_text.splitlines():
        stored_suffix, count = entry.split(':')
        if stored_suffix == hash_suffix:
            print(f"Password found! It has been breached {count} times.")
            return True

    print("Password not found in any breach data.")
    return False