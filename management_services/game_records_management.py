from management_services.read_write_users_data_functions import (
    read_from_personal_game_records,
    write_records_to_file,
)

records_dict = read_from_personal_game_records()


def get_user_game_records(username: str, records_file: dict) -> None:
    if username in records_file:
        games_records = records_file[username]

        for game, records in games_records.items():
            score = records["score"]
            print(f"{game}: {score}")

    else:
        print(f"Game records for {username} not found.")


def update_game_record(username: str, game_name: str, score: int, records_file: dict):
    if (
        username not in records_file
        or game_name not in records_file[username]
        or score is None
    ):
        records_file[username] = {game_name: {"score": score}}
        write_records_to_file(records_file)
        print(f"New score is {score}.")

    else:
        existing_score = records_file[username][game_name].get("score")

        if score > existing_score:
            records_file[username][game_name]["score"] = score
            write_records_to_file(records_file)
            print(f"New record for {game_name}: {score}")

        elif score == existing_score:
            print("You equaled the record!")

        elif score < existing_score:
            print("Try harder next time.")
