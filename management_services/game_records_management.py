def get_user_game_records(
    username: str, user_records: dict[str, int]
) -> dict[str, dict] | bool:
    if username in user_records:
        games_records = user_records[username]

        user_records = {"records": {}}

        for game, records in games_records.items():
            score = records["score"]
            user_records["records"][game] = {"score": score}

        return user_records

    else:
        return False


def update_game_record(
    username: str, game_name: str, score: int, user_records: dict[str, dict]
) -> bool:
    records_data = user_records

    if score is not None:
        if username not in records_data:
            records_data[username] = {}

        if game_name not in records_data[username]:
            records_data[username][game_name] = {"score": score}
            return True

        existing_record = records_data[username][game_name].get("score")
        if score >= existing_record:
            records_data[username][game_name]["score"] = score
            return True

    return False
