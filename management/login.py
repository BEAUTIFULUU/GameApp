from typing import Tuple


def read_accounts_from_file(filename='../users_data/accounts.py'):
    try:
        accounts_data = {}
        with open(filename, 'r') as file:
            exec(file.read(), {}, accounts_data)
        return accounts_data.get('accounts', {})
    except FileNotFoundError:
        print('Accounts file not found.')


acc_file = read_accounts_from_file()


def validate_credentials(username: str, password: str) -> Tuple[str, str]:
    while True:
        if len(username) not in range(6, 16):
            print('Invalid username length')
            username = input('Username needs to be in range(6-16): ')
            continue

        elif len(password) not in range(8, 20):
            print('Invalid password length.')
            password = input('Password needs to be in range(8-20): ')
            continue

        else:
            return username, password


def login_into_acc(val_username: str, val_password: str) -> None:
    if val_username in acc_file.keys() and val_password == acc_file[val_username]['password']:
        acc_token = acc_file[val_username]['token']
        print(f'Logged successfully. Your token: {acc_token}')

    else:
        print('Username or password invalid.')
