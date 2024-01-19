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


def start_app() -> None:
    while True:
        accounts = read_data_from_file(
            filename="users_data/accounts.json", dict_key="accounts"
        )
        auth_user_decision_str = get_valid_input(
            "1 - Login, 2 - Register, 0 - Exit: ",
            "Invalid input. Please enter a number.",
        )
        auth_user_decision = int(auth_user_decision_str)

        if auth_user_decision == 1:
            log_username = input("Enter username: ")
            log_password = input("Enter password: ")
            login_result = login_into_acc(
                username=log_username, password=log_password, accounts=accounts
            )

            if login_result is False:
                print("Invalid login credentials.")
                continue

            elif login_result:
                while True:
                    user_rec_file = read_data_from_file(
                        filename="users_data/personal_game_records.json",
                        dict_key="records",
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
                            game_score = number_guess_game(first_num, second_num)
                            update_result = update_game_record(
                                username=log_username,
                                game_name="Guess_Number_Game",
                                records_file=user_rec_file,
                                score=game_score,
                            )

                            if update_result is not False:
                                write_data_to_file(
                                    update_result,
                                    filename="users_data/personal_game_records.json",
                                    data_key="records",
                                )
                                print(
                                    f"Congratulations! You scored {game_score} in the Guess Number Game."
                                )
                                continue

                            else:
                                print("Try harder next time.")
                                continue

                    elif logged_usr_decision == 4:
                        print("Exiting...")
                        break

                    elif logged_usr_decision == 2:
                        user_records_result = get_user_game_records(
                            username=log_username, records_file=user_rec_file
                        )

                        if user_records_result is not False:
                            print(user_records_result)
                            continue

                        else:
                            print(f"Records for {log_username} not found.")

            else:
                continue

        elif auth_user_decision == 2:
            reg_username = input("Enter username: ")
            reg_login = input("Enter login: ")
            reg_password = input("Enter password: ")
            register_result, register_msg = register_acc(
                username=reg_username,
                login=reg_login,
                password=reg_password,
                accounts=accounts
            )

            if register_result is False:
                print(f"{register_msg}")
                continue

            else:
                write_data_to_file(
                    register_result,
                    filename="users_data/accounts.json",
                    data_key="accounts",
                )
                print(f"{register_msg}")
                continue

        elif auth_user_decision == 0:
            print("Exiting...")
            break


start_app()
