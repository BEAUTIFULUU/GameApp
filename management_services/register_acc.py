import uuid
from management_services.read_write_users_data_functions import write_accounts_to_file, read_accounts_from_file
from validation_services.validate_registration import (
    validate_username,
    validate_login,
    validate_password,
)

acc_file = read_accounts_from_file()


def register_account(
        validated_username: str, validated_login: str, validated_password: str
) -> bool:
    validated_username = validate_username(
        username=validated_username, accounts_file_dct=acc_file
    )
    validated_login = validate_login(
        username=validated_username,
        user_login=validated_login,
        accounts_file_dct=acc_file,
    )
    validated_password = validate_password(
        user_password=validated_password, accounts_file_dct=acc_file
    )

    if validated_login is not None and validated_password is not None:
        accounts_data = acc_file
        unique_token = str(uuid.uuid4())
        accounts_data[validated_username] = {
            "login": validated_login,
            "password": validated_password,
            "token": unique_token,
        }
        write_accounts_to_file(accounts_data)
        print(f"Account with login: {validated_login} registered.")
        return True

    else:
        print("Account registration failed.")
        return False
