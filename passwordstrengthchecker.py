import re

def check_password_strength(password):
    if len(password) < 8 or len(password) > 50:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

def main():
    print("Welcome to Easton's Password Checker")
    file_path = input("Enter the file path: ")

    try:
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
            weak_passwords = []
            for line in lines:
                match = re.match(r'\s*([^:]+):\s*(.*)', line)
                if match:
                    username = match.group(1)
                    password = match.group(2)
                    if not check_password_strength(password):
                        weak_passwords.append((username, password))
    except FileNotFoundError:
        print("No file found")
        return

    print("Weak passwords:")
    for username, password in weak_passwords:
        print("Username:", username)
        print("Password:", password)
        print()

if __name__ == '__main__':
    main()
