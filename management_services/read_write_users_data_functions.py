import json
import os


def read_data_from_file(filename: str):
    with open(filename, "r") as file:
        data = json.load(file)
        return data


def write_data_to_file(data_dict: dict, filename: str) -> None:
    with open(filename, "w") as file:
        json.dump(data_dict, file, indent=4)
