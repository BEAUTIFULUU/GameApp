from typing import Tuple

from management_services.read_write_users_data_functions import read_accounts_from_file

acc_file = read_accounts_from_file()


def validate_username(username: str, accounts_file_dct: dict) -> str | bool:
    min_digits = 2

    if len(username) not in range(6, 16):
        print("Invalid username lenght.")
        return False

    elif not sum(char.isdigit() for char in username) >= min_digits:
        print("At least two characters must be digits.")
        return False

    elif username in accounts_file_dct:
        print("Username already exists.")
        return False

    else:
        return username


def validate_login(
    user_login: str, accounts_file_dct: dict, username: str
) -> bool | str:
    if len(user_login) not in range(6, 16):
        print("Invalid password length.")
        return False

    elif not any(char.isdigit() for char in user_login):
        print("At least one character must be a digit.")
        return False

    elif any(data["login"] == user_login for data in accounts_file_dct.values()):
        print("Login already exists.")
        return False

    elif user_login == username:
        print("Login must be different than username and unique.")
        return False

    else:
        return user_login


def validate_password(user_password: str, accounts_file_dct: dict) -> bool | str:
    min_digits = 3

    if len(user_password) not in range(8, 20):
        print("Invalid password length.")
        return False

    elif not sum(char.isdigit() for char in user_password) >= min_digits:
        print("At least 3 characters in the password must be digits.")
        return False

    elif any(data["password"] == user_password for data in accounts_file_dct.values()):
        print("Invalid password.")
        return False

    else:
        return user_password
