from typing import Tuple

from games.number_guess_game import number_guess_game
from management_services.game_records_management import (
    get_user_game_records,
    update_game_record,
)
from management_services.login_acc import login_into_acc
from management_services.read_write_users_data_functions import write_data_to_file
from management_services.register_acc import register_acc
from management_services.update_user_credentials import (
    update_password_in_acc_dict,
    update_username_in_acc_dict,
)


def handle_user_login(
    username: str, password: str, accounts: dict[str, dict]
) -> Tuple[str, bool]:
    login_result = login_into_acc(
        username=username, password=password, accounts=accounts
    )
    if login_result is False:
        return "Invalid login credentials.", False
    elif login_result:
        return "Logged successfully.", True


def handle_user_registration(
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


def handle_guess_game_actions(
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


def handle_get_user_records(
    username: str, user_records: dict[str, dict]
) -> str | dict[str, dict]:
    user_records_result = get_user_game_records(
        username=username, user_records=user_records
    )
    if user_records_result is False:
        return "Personal records not found."

    elif user_records_result:
        return user_records_result


def handle_update_username(
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


def handle_update_password(new_password: str, username: str, accounts: dict[str, dict]):
    result = update_password_in_acc_dict(
        new_password=new_password,
        username=username,
        accounts=accounts,
    )
    if result is None:
        write_data_to_file(data_dict=accounts, filename="users_data/accounts.json")
        return "Password changed."
    return result
