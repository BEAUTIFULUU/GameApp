from typing import Tuple


def validate_login_credentials(username: str, password: str) -> Tuple[str, str]:
    while True:
        if len(username) not in range(6, 16):
            print("Invalid username length")
            username = input("Username needs to be in range(6-16): ")
            continue

        elif len(password) not in range(8, 20):
            print("Invalid password length.")
            password = input("Password needs to be in range(8-20): ")
            continue

        else:
            return username, password
