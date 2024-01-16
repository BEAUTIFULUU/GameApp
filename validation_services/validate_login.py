from typing import Tuple


def validate_login_credentials(username: str, password: str) -> bool | Tuple[str, str]:
    if len(username) not in range(6, 16):
        print("Invalid username length")
        return False

    elif len(password) not in range(8, 20):
        print("Invalid password length.")
        return False

    else:
        return username, password
