# main.py

from check_breach import check_password, check_multiple_passwords

def main():
    """
    Main function to run the password breach checker.
    Allows the user to choose between checking a single password or a list of passwords.
    """
    print("Welcome to the Password Breach Checker!")
    
    while True:
        print("\nSelect an option:")
        print("1. Check a single password")
        print("2. Check multiple passwords")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            password = input("Enter a password to check for breaches: ")
            check_password(password)
        
        elif choice == '2':
            # Accept multiple passwords, separated by commas
            passwords = input("Enter multiple passwords separated by commas: ").split(',')
            passwords = [password.strip() for password in passwords]  # Strip any extra spaces
            check_multiple_passwords(passwords)
        
        elif choice == '3':
            print("Exiting the program. Stay secure!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()