import json
import os


def read_data_from_file(filename: str, dict_key: str):
    accounts_data = {}

    if os.path.exists(filename):
        with open(filename, "r") as file:
            file_content = file.read()
            if file_content:
                accounts_data = json.loads(file_content)
            else:
                print(f"Error: File '{filename}'")

    return accounts_data.get(dict_key, {})


def write_data_to_file(data_dict: dict, filename: str, data_key: str) -> None:
    with open(filename, "w") as file:
        file.write(json.dumps({data_key: data_dict}, indent=4))
