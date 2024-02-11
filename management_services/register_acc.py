import uuid
from typing import Tuple

from validation_services.validate_registration import (
    validate_username,
    validate_login,
    validate_password,
)


def register_acc(
    username: str, login: str, password: str, accounts: dict[str, uuid]
) -> Tuple[bool, str] | Tuple[dict, str]:
    username_result = validate_username(
        username=username, accounts_file_dct=accounts
    )
    if username_result is not None:
        return False, f"Invalid username: {username_result}"

    login_result = validate_login(
        username=username,
        user_login=login,
        accounts_file_dct=accounts,
    )
    if login_result is not None:
        return False, f"Invalid login: {login_result}"

    password_result = validate_password(
        user_password=password, accounts_file_dct=accounts
    )
    if password_result is not None:
        return False, f"Invalid password: {password_result}"

    accounts_data = accounts
    unique_token = str(uuid.uuid4())
    accounts_data[username] = {
        "login": login,
        "password": password,
        "token": unique_token,
    }
    return accounts_data, "Account registered."
