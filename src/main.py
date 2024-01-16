from typing import Tuple

from management_services.read_write_users_data_functions import (
    read_accounts_from_file,
    write_records_to_file,
    read_from_personal_game_records,
    write_records_to_file)
from management_services.login_acc import login_into_acc
from management_services.register_acc import register_acc
from games.number_guess_game import number_guess_game
from validation_services.validate_user_decision_input import get_valid_input

accounts = read_accounts_from_file()


def _login_to_acc(log_username: str, log_password: str, log_acc_file: dict) -> bool | Tuple[str, str]:
    login_result = login_into_acc(username_to_val=log_username, password_to_val=log_password, acc_file=log_acc_file)
    return login_result


def _register_account(reg_surname: str, reg_login: str, reg_password: str) -> bool | Tuple[str, str, str]:
    return register_acc(username_to_val=reg_surname, login_to_val=reg_login, password_to_val=reg_password)


def _num_guess_game(first_num: int, second_num: int) -> int:
    return number_guess_game(first_num, second_num)


def start_app():
    while True:
        reload_acc_file = read_accounts_from_file()

        auth_user_decision_str = get_valid_input(
            "1 - Login, 2 - Register, 0 - Exit: ", "Invalid input. Please enter a number.")
        auth_user_decision = int(auth_user_decision_str)

        if auth_user_decision == 1:
            log_username = input("Enter username: ")
            log_password = input("Enter password: ")
            login_result = _login_to_acc(log_username, log_password, reload_acc_file)

            if login_result:
                while True:
                    logged_usr_decision_str = get_valid_input(
                        "1 - Games, 2 - Personal games records, 3 - Change account credentials, 4 - Exit",
                        "Invalid input. Please enter a number."
                    )
                    logged_usr_decision = int(logged_usr_decision_str)

                    if logged_usr_decision == 1:
                        user_game_choice_str = get_valid_input(
                            "1 - Guess Number Game, 2 - x, 3 - x", "Invalid input. Please enter a number.")
                        user_game_choice = int(user_game_choice_str)

                        if user_game_choice == 1:
                            first_num = int(input("Select number from 1 to 100: "))
                            second_num = int(
                                input("Select number from 1 to 100 bigger than the first one: ")
                            )
                            game_result = _num_guess_game(first_num, second_num)
                            continue

                        elif user_game_choice == 4:
                            print("Exiting...")
                            break

            else:
                continue

        elif auth_user_decision == 2:
            reg_username = input("Enter username: ")
            reg_login = input("Enter login: ")
            reg_password = input("Enter password: ")
            register_result = _register_account(reg_username, reg_login, reg_password)

            if register_result:
                continue

            else:
                continue


start_app()
