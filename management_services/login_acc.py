from typing import Tuple
from management_services.read_write_users_data_functions import read_accounts_from_file
from validation_services.validate_login import validate_login_credentials

accounts_file = read_accounts_from_file()


def login_into_acc(
    username_to_val: str, password_to_val: str
) -> bool | Tuple[str, str]:
    login_result = validate_login_credentials(username_to_val, password_to_val)

    if login_result:
        username, password = login_result
        if (
            username in accounts_file.keys()
            and password == accounts_file[username]["password"]
        ):
            acc_token = accounts_file[username]["token"]
            print(f"Logged successfully. Your token: {acc_token}")
            return username, password

    print("Username or password invalid.")
    return False
