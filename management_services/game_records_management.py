def get_user_game_records(username: str, records_file: dict) -> dict[str, dict] | bool:
    if username in records_file:
        games_records = records_file[username]

        user_records = {"records": {}}

        for game, records in games_records.items():
            score = records["score"]
            user_records["records"][game] = {"score": score}

        return user_records

    else:
        return False


def update_game_record(
    username: str, game_name: str, score: int, records_file: dict
) -> dict | bool:
    records_data = records_file

    if username not in records_data and score is not None:
        records_data[username] = {game_name: {"score": score}}
        return records_data

    existing_record = records_data[username][game_name].get("score")

    if username in records_data and score >= existing_record:
        records_data[username][game_name]["score"] = score
        return records_data

    return False
