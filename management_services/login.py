from validation_services.validate_login import validate_login_credentials


def login_into_acc(val_username: str, val_password: str, acc_file: dict) -> bool:
    username, password = validate_login_credentials(val_username, val_password)

    if username in acc_file.keys() and password == acc_file[username]["password"]:
        acc_token = acc_file[username]["token"]
        print(f"Logged successfully. Your token: {acc_token}")
        return True
    else:
        print("Username or password invalid.")
        return False
