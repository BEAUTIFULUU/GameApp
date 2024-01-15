from validation_services.validate_login import validate_login_credentials


def read_accounts_from_file(filename='../users_data/accounts.py'):
    try:
        accounts_data = {}
        with open(filename, 'r') as file:
            exec(file.read(), {}, accounts_data)
        return accounts_data.get('accounts', {})
    except FileNotFoundError:
        print('Accounts file not found.')


acc_file = read_accounts_from_file()


def login_into_acc(val_username: str, val_password: str) -> bool:
    username, password = validate_login_credentials(val_username, val_password)

    if username in acc_file.keys() and password == acc_file[username]['password']:
        acc_token = acc_file[username]['token']
        print(f'Logged successfully. Your token: {acc_token}')
        return True
    else:
        print('Username or password invalid.')
        return False
