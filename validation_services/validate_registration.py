from management_services.read_write_users_data_functions import read_accounts_from_file

acc_file = read_accounts_from_file()


def validate_username(username: str, accounts_file_dct: dict) -> str | None:
    min_digits = 2
    while True:
        if len(username) not in range(6, 16):
            print("Invalid username lenght.")
            username = input("Username(must be unique, lenght(6-16), min. 2 digits):")
            continue

        elif not sum(char.isdigit() for char in username) >= min_digits:
            print("At least two characters must be digits.")
            username = input("Username(must be unique, lenght(6-16), min. 2 digits):")
            continue

        elif username in accounts_file_dct:
            print("Username already exists.")
            username = input("Username(must be unique, length(6-16), min. 2 digits):")
            continue

        else:
            return username


def validate_login(
    user_login: str, accounts_file_dct: dict, username: str
) -> str | None:
    while True:
        if len(user_login) not in range(6, 16):
            print("Invalid password length.")
            user_login = input("Login(must be unique, length(6-16), min. 1 digit): ")
            continue

        elif not any(char.isdigit() for char in user_login):
            print("At least one character must be a digit.")
            user_login = input("Login(must be unique, length(6-16), min. 1 digit): ")
            continue

        elif any(data["login"] == user_login for data in accounts_file_dct.values()):
            print("Login already exists.")
            user_login = input("Login(must be unique, length(6-16), min. 1 digit): ")
            continue

        elif user_login == username:
            print("Login must be different than username and unique.")
            user_login = input("Login(must be unique, length(6-16), min. 1 digit): ")
            continue

        else:
            return user_login


def validate_password(user_password: str, accounts_file_dct: dict) -> str | None:
    min_digits = 3

    while True:
        if len(user_password) not in range(8, 20):
            print("Invalid password length.")
            user_password = input(
                "Password(must be unique, length(8-20), min 3 digits, min 1 uppercase): "
            )
            continue

        elif not sum(char.isdigit() for char in user_password) >= min_digits:
            print("At least 3 characters in the password must be digits.")
            user_password = input(
                "Password(must be unique, length(8-20), min 3 digits, min 1 uppercase): "
            )
            continue

        elif any(
            data["password"] == user_password for data in accounts_file_dct.values()
        ):
            print("Invalid password.")
            user_password = input(
                "Password(must be unique, length(8-20), min 3 digits, min 1 uppercase): "
            )
            continue

        else:
            return user_password
