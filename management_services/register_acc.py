import uuid
from validation_services.validate_registration import (
    validate_username,
    validate_login,
    validate_password,
)


def register_acc(
    username_to_val, login_to_val: str, password_to_val: str, accounts: dict
) -> dict | bool:
    if not validate_username(username=username_to_val, accounts_file_dct=accounts):
        return False

    elif not validate_login(
        username=username_to_val,
        user_login=login_to_val,
        accounts_file_dct=accounts,
    ):
        return False

    elif not validate_password(user_password=password_to_val, accounts_file_dct=accounts):
        return False

    else:
        accounts_data = accounts
        unique_token = str(uuid.uuid4())
        accounts_data[username_to_val] = {
            "login": login_to_val,
            "password": password_to_val,
            "token": unique_token,
        }
        return accounts_data
