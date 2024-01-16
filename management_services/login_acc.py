from typing import Tuple

from validation_services.validate_login import validate_login_credentials


def login_into_acc(username_to_val: str, password_to_val: str, acc_file: dict) -> bool | Tuple[str, str]:
    login_result = validate_login_credentials(username_to_val, password_to_val)

    if login_result:
        username, password = login_result
        if username in acc_file.keys() and password == acc_file[username]["password"]:
            acc_token = acc_file[username]["token"]
            print(f"Logged successfully. Your token: {acc_token}")
            return username, password

    print("Username or password invalid.")
    return False
