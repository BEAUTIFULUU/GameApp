def validate_new_username(new_username: str, login: str, accounts: dict[str, dict]):
    min_digits = 2

    if len(new_username) not in range(6, 16):
        return "Username must be in range (6-15)"

    elif not sum(char.isdigit() for char in new_username) >= min_digits:
        return "Username must have at least 3 digits."

    elif new_username in accounts:
        return "Username already exists."

    elif new_username == login:
        return "Username needs to be different from login."

    else:
        return None
