def validate_new_username(
    new_username: str, login: str, accounts: dict[str, dict]
) -> ValueError | None:
    min_digits = 2

    if len(new_username) not in range(6, 16) or new_username is None:
        raise ValueError("Username needs to be in range 6-15.")

    elif not sum(char.isdigit() for char in new_username) >= min_digits:
        raise ValueError("Username must have at least 3 digits.")

    elif new_username in accounts:
        raise ValueError("Username already exists.")

    elif new_username == login:
        raise ValueError("Username needs to be different from login.")

    else:
        return None
