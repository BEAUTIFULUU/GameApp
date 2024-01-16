import uuid
from typing import Tuple

from management_services.read_write_users_data_functions import (
    write_accounts_to_file,
    read_accounts_from_file,
)
from validation_services.validate_registration import (
    validate_username,
    validate_login,
    validate_password,
)

acc_file = read_accounts_from_file()


def register_acc(
        username_to_val: str, login_to_val: str, password_to_val: str
) -> bool | Tuple[str, str, str]:
    validated_username = validate_username(
        username=username_to_val, accounts_file_dct=acc_file
    )
    validated_login = validate_login(
        username=validated_username,
        user_login=login_to_val,
        accounts_file_dct=acc_file,
    )
    validated_password = validate_password(
        user_password=password_to_val, accounts_file_dct=acc_file
    )

    if not all((validated_username, validated_login, validated_password)):
        print("Account registration failed due to validation errors.")
        return False

    accounts_data = acc_file
    unique_token = str(uuid.uuid4())
    accounts_data[validated_username] = {
        "login": validated_login,
        "password": validated_password,
        "token": unique_token,
    }
    write_accounts_to_file(accounts_data)
    print(f"Account with login: {validated_login} registered.")
    return validated_username, validated_login, validated_password
