import json
import os


def read_accounts_from_file(filename="../users_data/accounts.json"):
    accounts_data = {}

    if os.path.exists(filename):
        with open(filename, "r") as file:
            file_content = file.read()
            if file_content:
                accounts_data = json.loads(file_content)
            else:
                print(f"Error: File '{filename}'")

    return accounts_data.get("accounts", {})


def write_accounts_to_file(
    accounts_dict: dict, filename="../users_data/accounts.json"
) -> None:
    with open(filename, "w") as file:
        file.write(json.dumps({"accounts": accounts_dict}, indent=4))


def read_from_personal_game_records(
    filename="../users_data/personal_game_records.json",
):
    personal_game_records = {}

    if os.path.exists(filename):
        with open(filename, "r") as file:
            file_content = file.read()
            if file_content:
                personal_game_records = json.loads(file_content)
            else:
                print(f"Error: File '{filename}'.")

    return personal_game_records.get("records", {})


def write_records_to_file(
    records_dict: dict, filename="../users_data/personal_game_records.json"
) -> None:
    with open(filename, "w") as file:
        file.write(json.dumps({"records": records_dict}, indent=4))
