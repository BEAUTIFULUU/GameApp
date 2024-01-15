from games.number_guess_game import number_guess_game
from management_services.login import login_into_acc
from management_services.register_acc import register_account


def read_from_personal_game_records(filename: str = '../users_data/personal_game_records.py'):
    try:
        personal_game_records = {}
        with open(filename, 'r') as file:
            exec(file.read(), {}, personal_game_records)
        return personal_game_records.get('records', {})
    except FileNotFoundError:
        print('Records file not found.')


pers_game_records = read_from_personal_game_records()


def start_user_auth() -> str | None:
    while True:
        user_decision_str = input('1 - Login, 2 - Register, 0 - Exit: ')

        if not user_decision_str.isdigit():
            print('Invalid input. Please enter a number.')
            continue

        user_decision = int(user_decision_str)

        if user_decision == 1:
            username = input('Enter username: ')
            password = input('Enter password: ')
            logged = login_into_acc(val_username=username, val_password=password)
            if logged:
                return username

        elif user_decision == 2:
            username = input('Username(must be unique, lenght(6-16), min. 2 digits): ')
            login = input('Login(must be unique, length(6-16), min. 1 digit): ')
            password = input('Password(must be unique, length(8-20), min 3 digits, min 1 uppercase): ')
            register_account(validated_username=username, validated_login=login, validated_password=password)

        elif user_decision == 0:
            print('Exiting...')
            break

        else:
            print('Invalid choice. Please enter 1 for login or 2 for registration.')


username = start_user_auth()

if username is not None:
    while True:
        user_decision_str = input('1 - Games, 2 - Personal records, 3 - Change account credentials, 4 - Exit: ')

        if not user_decision_str.isdigit():
            print('Invalid input. Please enter a number.')
            continue

        user_decision = int(user_decision_str)

        if user_decision == 1:
            number_guess_game()

        elif user_decision == 2:
            if username in pers_game_records:
                user_records = pers_game_records[username]

                for game, details in user_records.items():
                    score = details['score']
                    print(f'{game}: {score}')

            else:
                print('Records not found.')
