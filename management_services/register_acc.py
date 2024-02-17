import uuid
from validation_services.validate_user_credentials import (
    validate_username,
    validate_password,
)


def register_acc(
    username: str, password: str, accounts: dict[str, uuid]
) -> Exception | dict[str, str]:
    username_exception = validate_username(
        username=username, accounts_file_dct=accounts
    )
    if username_exception is not None:
        return username_exception

    password_exception = validate_password(
        user_password=password, accounts_file_dct=accounts
    )
    if password_exception is not None:
        return password_exception

    accounts_data = accounts
    unique_token = str(uuid.uuid4())
    accounts_data[username] = {
        "password": password,
        "token": unique_token,
    }
    return accounts_data
