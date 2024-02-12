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
        assert result is not False

    def test_if_username_not_in_records_return_false(self, open_records_dict):
        records_dict = open_records_dict
        result = get_user_game_records(
            username="testuser321", user_records=records_dict
        )
        assert result is False
