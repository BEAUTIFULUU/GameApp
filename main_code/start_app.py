from games.number_guess_game import number_guess_game
from management_services.login import login_into_acc
from management_services.read_write_users_data_functions import (
    read_accounts_from_file,
    read_from_personal_game_records,
    write_records_to_file,
)
from management_services.register_acc import register_account


pers_game_records = read_from_personal_game_records()


def start_user_auth() -> str | None:
    while True:
        reload_acc_file = read_accounts_from_file()
        user_decision_str_auth = input("1 - Login, 2 - Register, 0 - Exit: ")

        if not user_decision_str_auth.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        user_decision_auth = int(user_decision_str_auth)

        if user_decision_auth == 1:
            username_auth = input("Enter username: ")
            password = input("Enter password: ")
            logged = login_into_acc(
                val_username=username_auth,
                val_password=password,
                acc_file=reload_acc_file,
            )
            if logged:
                return username_auth

        elif user_decision_auth == 2:
            username_auth = input(
                "Username(must be unique, length(6-16), min. 2 digits): "
            )
            login = input("Login(must be unique, length(6-16), min. 1 digit): ")
            password = input(
                "Password(must be unique, length(8-20), min 3 digits, min 1 uppercase): "
            )
            register_account(
                validated_username=username_auth,
                validated_login=login,
                validated_password=password,
            )

        elif user_decision_auth == 0:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1 for login or 2 for registration.")


username = start_user_auth()

if username is not None:
    while True:
        user_decision_str = input(
            "1 - Games, 2 - Personal records, 3 - Change account credentials, 4 - Exit: "
        )

        if not user_decision_str.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        user_decision = int(user_decision_str)

        if user_decision == 1:
            user_game_choice_str = input("1 - Guess the num, 2 - x, 3 - x")

            if not user_game_choice_str.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            user_game_choice = int(user_game_choice_str)

            if user_game_choice == 1:
                game_score = number_guess_game()
                game_records = read_from_personal_game_records()

                if username not in game_records.keys() and game_score is not None:
                    game_records[username] = {"Guess_the_num": {"score": game_score}}
                    write_records_to_file(records_dict=game_records)
                    print(f"First record: {game_score}")
                    continue

                existing_record = game_records[username]["Guess_the_num"].get("score")

                if username in game_records and game_score > existing_record:
                    game_records[username]["Guess_the_num"]["score"] = game_score
                    write_records_to_file(records_dict=game_records)
                    print(f"Congratulations ! Your new record is: {game_score}")
                    continue

                elif username in game_records and game_score == existing_record:
                    print("You equaled the record!")
                    continue

                elif username in game_records and game_score < existing_record:
                    print("Try harder next time.")
                    continue

        elif user_decision == 2:
            pers_game_records = read_from_personal_game_records()
            if username in pers_game_records:
                user_records = pers_game_records[username]

                for game, details in user_records.items():
                    score = details["score"]
                    print(f"{game}: {score}")
                    continue

            else:
                print("Records not found.")
