from management_services.main_handlers import (
    handle_user_login,
    handle_user_registration,
    handle_guess_game_actions,
    handle_update_username,
    handle_update_password,
    handle_get_user_records,
)
from management_services.read_write_users_data_functions import read_data_from_file
from validation_services.validate_user_decision_input import get_valid_input


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
                login_msg, login_result = handle_user_login(
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
                    register_result = handle_user_registration(
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
                        input("Select number from 1 to 100 bigger than the first one: ")
                    )
                    game_score = handle_guess_game_actions(
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
                        update_message = handle_update_username(
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
                        update_message = handle_update_password(
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
                user_records = handle_get_user_records(
                    username=log_username, user_records=user_records
                )
                print(user_records)


start_app()
