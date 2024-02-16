def validate_username(
    username: str, accounts_file_dct: dict[str, dict]
) -> ValueError | None:
    min_digits = 2

    if len(username) not in range(6, 16):
        raise ValueError("Username must be in range 6-15.")

    elif not sum(char.isdigit() for char in username) >= min_digits:
        raise ValueError("Username must have at least 2 digits.")

    elif username in accounts_file_dct:
        raise ValueError("Username already exists.")

    else:
        return None


def validate_login(
    user_login: str, accounts_file_dct: dict[str, dict], username: str
) -> ValueError | None:
    if len(user_login) not in range(6, 16):
        raise ValueError("Login must be in range 6-15.")

    elif not any(char.isdigit() for char in user_login):
        raise ValueError("Login must have at least 1 digit.")

    elif any(data["login"] == user_login for data in accounts_file_dct.values()):
        raise ValueError("Login already exists.")

    elif user_login == username:
        raise ValueError("Login must be different from username.")

    else:
        return None


def validate_password(
    user_password: str, accounts_file_dct: dict[str, dict]
) -> ValueError | None:
    min_digits = 3

    if len(user_password) not in range(8, 20):
        raise ValueError("Password must be in range 8-19.")

    elif not sum(char.isdigit() for char in user_password) >= min_digits:
        raise ValueError("Password must contain at least 3 digits.")

    elif any(data["password"] == user_password for data in accounts_file_dct.values()):
        raise ValueError("Invalid password.")

    else:
        return None
