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
) -> dict | bool:
    if user_records is None:
        user_records = {}

    if score is not None:
        if username not in user_records:
            user_records[username] = {}

        if game_name not in user_records[username]:
            user_records[username][game_name] = {"score": score}
            return user_records

        existing_record = user_records[username][game_name].get("score")
        if score >= existing_record:
            user_records[username][game_name]["score"] = score
            return user_records

        if score < existing_record:
            return False
