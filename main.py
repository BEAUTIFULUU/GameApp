from typing import Tuple

from management_services.read_write_users_data_functions import (
    write_data_to_file,
    read_data_from_file,
)
from management_services.login_acc import login_into_acc
from management_services.register_acc import register_acc
from games.number_guess_game import number_guess_game
from validation_services.validate_user_decision_input import get_valid_input
from management_services.game_records_management import (
    update_game_record,
    get_user_game_records,
)
from management_services.update_user_credentials import update_acc_dict


def _handle_user_login(
    username: str, password: str, accounts: dict[str, str]
) -> Tuple[str, bool]:
    login_result = login_into_acc(
        username=username, password=password, accounts=accounts
    )
    if login_result is False:
        return "Invalid login credentials.", False
    elif login_result:
        return "Logged successfully.", True


def _handle_user_registration(
    username: str, login: str, password: str, accounts: dict[str, str]
) -> str:
    register_result, register_msg = register_acc(
        username=username,
        login=login,
        password=password,
        accounts=accounts,
    )

    if register_result is False:
        return register_msg

    elif register_result:
        write_data_to_file(
            data_dict=register_result,
            filename="users_data/accounts.json",
        )
        return register_msg


def _handle_guess_game_actions(
    username: str, user_records: dict[str, dict], first_num: int, second_num: int
) -> str:
    game_score = number_guess_game(first_num=first_num, second_num=second_num)
    update_result = update_game_record(
        username=username,
        game_name="Guess_Number_Game",
        user_records=user_records,
        score=game_score,
    )

    if update_result is not False and update_result is not None:
        write_data_to_file(
            data_dict=update_result,
            filename="users_data/personal_game_records.json",
        )
        return f"You scored {game_score} in the Guess Number Game."
    return "Try harder next time!"


def _get_user_records(username: str, user_records: dict[str, int]) -> str | dict:
    user_records_result = get_user_game_records(
        username=username, user_records=user_records
    )
    if user_records_result is False:
        return "Personal records not found"

    elif user_records_result:
        return user_records_result


def _update_username(
    username: str, new_username: str, accounts: dict[str, dict]
) -> str:
    update_message = update_acc_dict(
        username=username, new_username=new_username, accounts=accounts
    )

    write_data_to_file(
        data_dict=accounts,
        filename="users_data/accounts.json",
    )
    write_data_to_file(
        data_dict=accounts,
        filename="users_data/personal_game_records.json",
    )
    return update_message


def start_app() -> None:
    while True:
        accounts = read_data_from_file(
            filename="users_data/accounts.json",
        )
        auth_user_decision_str = get_valid_input(
            "1 - Login, 2 - Register, 0 - Exit: ",
            "Invalid input. Please enter a number.",
        )
        auth_user_decision = int(auth_user_decision_str)

        if auth_user_decision == 1:
            log_username = input("Enter username: ")
            log_password = input("Enter password: ")
            login_msg, login_result = _handle_user_login(
                username=log_username, password=log_password, accounts=accounts
            )
            print(login_msg)

            if login_result:
                while True:
                    user_records = read_data_from_file(
                        filename="users_data/personal_game_records.json",
                    )
                    logged_usr_decision_str = get_valid_input(
                        "1 - Games, 2 - Personal games records, 3 - Change account credentials, 4 - Exit: ",
                        "Invalid input. Please enter a number.",
                    )
                    logged_usr_decision = int(logged_usr_decision_str)

                    if logged_usr_decision == 1:
                        user_game_choice_str = get_valid_input(
                            "1 - Guess Number Game, 2 - x, 3 - x: ",
                            "Invalid input. Please enter a number.",
                        )
                        user_game_choice = int(user_game_choice_str)

                        if user_game_choice == 1:
                            first_num = int(input("Select number from 1 to 100: "))
                            second_num = int(
                                input(
                                    "Select number from 1 to 100 bigger than the first one: "
                                )
                            )
                            game_score = _handle_guess_game_actions(
                                username=log_username,
                                user_records=user_records,
                                first_num=first_num,
                                second_num=second_num,
                            )

                            print(game_score)
                            continue

                    elif logged_usr_decision == 3:
                        change_credentials_choice = get_valid_input(
                            prompt="1 - Change username, 2 - Change login, 3 - Change password, 4 - Exit: ",
                            error_message="Invalid input. Please enter a number.",
                        )
                        update_choice = int(change_credentials_choice)
                        if update_choice == 1:
                            new_username = input("Enter new username: ")
                            update_message = _update_username(
                                username=log_username,
                                new_username=new_username,
                                accounts=accounts,
                            )
                            print(update_message)
                        continue

                    elif logged_usr_decision == 4:
                        print("Exiting...")
                        break

                    elif logged_usr_decision == 2:
                        user_records = _get_user_records(
                            username=log_username, user_records=user_records
                        )
                        print(user_records)

            else:
                continue

        elif auth_user_decision == 2:
            reg_username = input("Enter username: ")
            reg_login = input("Enter login: ")
            reg_password = input("Enter password: ")
            register_result = _handle_user_registration(
                username=reg_username,
                login=reg_login,
                password=reg_password,
                accounts=accounts,
            )
            print(register_result)
            continue

        elif auth_user_decision == 0:
            print("Exiting...")
            break


start_app()
