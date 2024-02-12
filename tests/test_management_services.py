import pytest
from management_services.read_write_users_data_functions import read_data_from_file
from management_services.game_records_management import (
    get_user_game_records,
    update_game_record,
)


@pytest.fixture
def open_records_dict():
    records_dict = read_data_from_file(
        filename="tests/test_data/test_user_records.json", dict_key="records"
    )
    return records_dict


class TestGamesRecordsManagement:
    def test_if_username_in_records_return_records(self, open_records_dict):
        records_dict = open_records_dict
        result = get_user_game_records(
            username="testuser123", user_records=records_dict
        )
        assert "records" in result.keys()

    def test_if_username_not_in_records_return_false(self, open_records_dict):
        records_dict = open_records_dict
        result = get_user_game_records(
            username="testuser321", user_records=records_dict
        )
        assert result is False

    def test_update_game_record_create_new_record_if_username_not_in_records_and_game_record_not_in_records(
        self, open_records_dict
    ):
        records_dict = open_records_dict
        game_name = "test_game"
        game_score = 5
        username = "testuser123"
        assert username in records_dict
        assert game_name not in records_dict[username]
        update_game_record(
            username=username,
            game_name=game_name,
            score=game_score,
            user_records=records_dict,
        )

        assert game_name in records_dict[username]
        assert records_dict[username][game_name]["score"] == game_score

    def test_update_game_record_update_existing_record_if_new_score_is_bigger_than_record(
        self, open_records_dict
    ):
        records_dict = open_records_dict
        game_name = "Guess_Number_Game"
        game_score = 5
        username = "testuser123"
        assert username in records_dict
        assert game_name in records_dict[username]
        assert records_dict[username][game_name]["score"] == 4
        update_game_record(
            username=username,
            game_name=game_name,
            score=game_score,
            user_records=records_dict,
        )
        assert records_dict[username][game_name]["score"] == game_score

    def test_update_game_record_create_new_record_if_username_in_records_and_game_not_in_user_records(
        self, open_records_dict
    ):
        records_dict = open_records_dict
        game_name = "new_test_game"
        game_score = 2
        username = "testuser123"
        assert username in records_dict
        assert game_name not in records_dict[username]
        update_game_record(
            username=username,
            game_name=game_name,
            score=game_score,
            user_records=records_dict,
        )
        assert game_name in records_dict[username]
        assert records_dict[username][game_name]["score"] == game_score

    def test_update_game_record_does_not_update_record_if_score_lower_than_record(
        self, open_records_dict
    ):
        records_dict = open_records_dict
        game_name = "Guess_Number_Game"
        game_score = 3
        username = "testuser123"
        assert username in records_dict
        assert game_name in records_dict[username]
        existing_record = records_dict[username][game_name]["score"]
        assert existing_record > game_score
        update_game_record(
            username=username,
            game_name=game_name,
            score=game_score,
            user_records=records_dict,
        )
        assert records_dict[username][game_name]["score"] == existing_record

    def test_update_game_record_does_not_create_record_if_score_is_none_and_user_not_in_records(
        self, open_records_dict
    ):
        records_dict = open_records_dict
        game_name = "test_game"
        game_score = None
        username = "testuser321"
        assert username not in records_dict
        update_game_record(
            username=username,
            game_name=game_name,
            score=game_score,
            user_records=records_dict,
        )
        assert username not in records_dict
