import uuid
from validation_services.validate_registration import (
    validate_username,
    validate_login,
    validate_password,
)


def register_acc(
    username_to_val: str, login_to_val: str, password_to_val: str, accounts_file: dict
) -> dict | bool:
    validated_username = validate_username(
        username=username_to_val, accounts_file_dct=accounts_file
    )
    validated_login = validate_login(
        username=validated_username,
        user_login=login_to_val,
        accounts_file_dct=accounts_file,
    )
    validated_password = validate_password(
        user_password=password_to_val, accounts_file_dct=accounts_file
    )

    if not all((validated_username, validated_login, validated_password)):
        return False

    accounts_data = accounts_file
    unique_token = str(uuid.uuid4())
    accounts_data[validated_username] = {
        "login": validated_login,
        "password": validated_password,
        "token": unique_token,
    }
    return accounts_data
