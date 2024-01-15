import json


def read_accounts_from_file(filename="../users_data/accounts.py"):
    try:
        accounts_data = {}
        with open(filename, "r") as file:
            exec(file.read(), {}, accounts_data)
        return accounts_data.get("accounts", {})
    except FileNotFoundError:
        print("Accounts file not found.")


def write_accounts_to_file(
    accounts_dict: dict, filename="../users_data/accounts.py"
) -> None:
    with open(filename, "w") as file:
        file.write(f"accounts = {json.dumps(accounts_dict, indent=4)}\n")


def read_from_personal_game_records(
    filename: str = "../users_data/personal_game_records.py",
):
    try:
        personal_game_records = {}
        with open(filename, "r") as file:
            exec(file.read(), {}, personal_game_records)
        return personal_game_records.get("records", {})
    except FileNotFoundError:
        print("Records file not found.")