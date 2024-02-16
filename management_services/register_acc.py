import uuid
from validation_services.validate_registration import (
    validate_username,
    validate_login,
    validate_password,
)


def register_acc(
    username: str, login: str, password: str, accounts: dict[str, uuid]
) -> Exception | dict[str, str]:
    username_exception = validate_username(
        username=username, accounts_file_dct=accounts
    )
    if username_exception is not None:
        return username_exception

    login_exception = validate_login(
        username=username,
        user_login=login,
        accounts_file_dct=accounts,
    )
    if login_exception is not None:
        return login_exception

    password_exception = validate_password(
        user_password=password, accounts_file_dct=accounts
    )
    if password_exception is not None:
        return password_exception

    accounts_data = accounts
    unique_token = str(uuid.uuid4())
    accounts_data[username] = {
        "login": login,
        "password": password,
        "token": unique_token,
    }
    return accounts_data
