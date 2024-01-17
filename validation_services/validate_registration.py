def validate_username(username: str, accounts_file_dct: dict) -> str | bool:
    min_digits = 2

    if len(username) not in range(6, 16):
        return False

    elif not sum(char.isdigit() for char in username) >= min_digits:
        return False

    elif username in accounts_file_dct:
        return False

    else:
        return username


def validate_login(
    user_login: str, accounts_file_dct: dict, username: str
) -> bool | str:
    if len(user_login) not in range(6, 16):
        return False

    elif not any(char.isdigit() for char in user_login):
        return False

    elif any(data["login"] == user_login for data in accounts_file_dct.values()):
        return False

    elif user_login == username:
        return False

    else:
        return user_login


def validate_password(user_password: str, accounts_file_dct: dict) -> bool | str:
    min_digits = 3

    if len(user_password) not in range(8, 20):
        return False

    elif not sum(char.isdigit() for char in user_password) >= min_digits:
        return False

    elif any(data["password"] == user_password for data in accounts_file_dct.values()):
        return False

    else:
        return user_password
