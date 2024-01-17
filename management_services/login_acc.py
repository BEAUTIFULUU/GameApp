from validation_services.validate_login import validate_login_credentials


def login_into_acc(username_to_val: str, password_to_val: str, accounts_file: dict):
    login_result = validate_login_credentials(username_to_val, password_to_val)

    if login_result:
        username, password = login_result
        if (
            username in accounts_file.keys()
            and password == accounts_file[username]["password"]
        ):
            acc_token = accounts_file[username]["token"]
            return username, password, acc_token

    return False
