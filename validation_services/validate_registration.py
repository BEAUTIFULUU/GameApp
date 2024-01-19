from typing import Tuple


def validate_username(username: str, accounts_file_dct: dict) -> Tuple[bool, str] | bool:
    min_digits = 2

    if len(username) not in range(6, 16):
        return False, "Username must be in range (6-16)"

    elif not sum(char.isdigit() for char in username) >= min_digits:
        return False, "Username must have at least 3 digits."

    elif username in accounts_file_dct:
        return False, "Username already exists."

    else:
        return True


def validate_login(
    user_login: str, accounts_file_dct: dict, username: str
) -> Tuple[bool, str] | bool:
    if len(user_login) not in range(6, 16):
        return False, "Login needs to be in range (6-16)"

    elif not any(char.isdigit() for char in user_login):
        return False, "Login must have at least 1 digit. "

    elif any(data["login"] == user_login for data in accounts_file_dct.values()):
        return False, "Login already exist."

    elif user_login == username:
        return False, "Login needs to be different than username."

    else:
        return True


def validate_password(user_password: str, accounts_file_dct: dict) -> Tuple[bool, str] | bool:
    min_digits = 3

    if len(user_password) not in range(8, 20):
        return False, "Password needs to be in range (8-20)"

    elif not sum(char.isdigit() for char in user_password) >= min_digits:
        return False, "Password must have at least 3 digits."

    elif any(data["password"] == user_password for data in accounts_file_dct.values()):
        return False, "Invalid password"

    else:
        return True
