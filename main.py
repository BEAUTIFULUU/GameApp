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
from management_services.update_user_credentials import (
    update_username_in_acc_dict,
    update_password_in_acc_dict,
)


def _handle_user_login(
        username: str, password: str, accounts: dict[str, dict]
) -> Tuple[str, bool]:
    login_result = login_into_acc(
        username=username, password=password, accounts=accounts
    )
    if login_result is False:
        return "Invalid login credentials.", False
    elif login_result:
        return "Logged successfully.", True


def _handle_user_registration(
        username: str, password: str, accounts: dict[str, str]
) -> ValueError | str:
    register_result = register_acc(
        username=username,
        password=password,
        accounts=accounts,
    )

    if isinstance(register_result, ValueError):
        return register_result

    elif not isinstance(register_result, ValueError):
        write_data_to_file(
            data_dict=register_result,
            filename="users_data/accounts.json",
        )
        return "Account registered."


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


def _handle_get_user_records(
        username: str, user_records: dict[str, dict]
) -> str | dict[str, dict]:
    user_records_result = get_user_game_records(
        username=username, user_records=user_records
    )
    if user_records_result is False:
        return "Personal records not found"

    elif user_records_result:
        return user_records_result


def _handle_update_username(
        username: str,
        new_username: str,
        accounts: dict[str, dict],
        records: dict[str, dict],
) -> ValueError | str:
    result = update_username_in_acc_dict(
        username=username, new_username=new_username, accounts=accounts, records=records
    )
    if result is None:
        write_data_to_file(
            data_dict=accounts,
            filename="users_data/accounts.json",
        )
        write_data_to_file(
            data_dict=records,
            filename="users_data/personal_game_records.json",
        )
        return f"Username changed to {new_username}."
    return result


def _handle_update_password(
        new_password: str, username: str, accounts: dict[str, dict]
):
    result = update_password_in_acc_dict(
        new_password=new_password,
        username=username,
        accounts=accounts,
    )
    if result is None:
        write_data_to_file(data_dict=accounts, filename="users_data/accounts.json")
        return "Password changed."
    return result


def start_app() -> None:
    user_state = "not_logged_in"
    log_username = None
    accounts = None

    while True:
        if user_state == "not_logged_in":
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
                    user_state = "logged_in"
                continue

            elif auth_user_decision == 2:
                reg_username = input("Enter username: ")
                reg_password = input("Enter password: ")
                try:
                    register_result = _handle_user_registration(
                        username=reg_username,
                        password=reg_password,
                        accounts=accounts,
                    )
                    print(register_result)

                except ValueError as e:
                    print(f"Error: {e}")
                    continue

            elif auth_user_decision == 0:
                print("Exiting...")
                break

        elif user_state == "logged_in":
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
                    prompt="1 - Change username, 2 - Change password, 3 - Exit: ",
                    error_message="Invalid input. Please enter a number.",
                )
                update_choice = int(change_credentials_choice)
                if update_choice == 1:
                    new_username = input("Enter new username: ")
                    try:
                        update_message = _handle_update_username(
                            username=log_username,
                            new_username=new_username,
                            accounts=accounts,
                            records=user_records,
                        )
                        print(update_message)
                        log_username = new_username
                    except ValueError as e:
                        print(f"Error: {e}")
                        continue

                elif update_choice == 2:
                    new_password = input("Enter new password: ")
                    try:
                        update_message = _handle_update_password(
                            new_password=new_password,
                            username=log_username,
                            accounts=accounts,
                        )
                        print(update_message)
                    except ValueError as e:
                        print(f"Error: {e}")
                        continue

            elif logged_usr_decision == 4:
                print("Exiting...")
                user_state = "not_logged_in"
                continue

            elif logged_usr_decision == 2:
                user_records = _handle_get_user_records(
                    username=log_username, user_records=user_records
                )
                print(user_records)


start_app()

