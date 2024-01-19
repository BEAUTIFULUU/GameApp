import uuid
from typing import Tuple

from validation_services.validate_registration import (
    validate_username,
    validate_login,
    validate_password,
)


def register_acc(
    username: str, login: str, password: str, accounts: dict
) -> Tuple[bool, str] | dict:
    username_valid, username_msg = validate_username(
        username=username, accounts_file_dct=accounts
    )
    if not username_valid:
        return False, f"Invalid username: {username_msg}"

    login_valid, login_msg = validate_login(
        username=username,
        user_login=login,
        accounts_file_dct=accounts,
    )
    if not login_valid:
        return False, f"Invalid login: {login_msg}"

    password_valid, password_msg = validate_password(
        user_password=password, accounts_file_dct=accounts
    )
    if not password_valid:
        return False, f"Invalid password: {password_msg}"

    accounts_data = accounts
    unique_token = str(uuid.uuid4())
    accounts_data[username] = {
        "login": login,
        "password": password,
        "token": unique_token,
    }
    return accounts_data
