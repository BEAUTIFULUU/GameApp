import pytest
from management_services.read_write_users_data_functions import read_data_from_file
from management_services.game_records_management import (
    get_user_game_records,
    update_game_record,
)
from management_services.login_acc import login_into_acc
from management_services.register_acc import register_acc


@pytest.fixture
def open_records_dict():
    records_dict = read_data_from_file(
        filename="tests/test_data/test_user_records.json"
    )
    return records_dict


@pytest.fixture
def open_accounts_dict():
    accounts_dict = read_data_from_file(filename="tests/test_data/test_accounts.json")
    return accounts_dict


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


class TestLoginManagement:
    def test_login_into_acc_return_true_if_username_and_password_are_valid(
        self, open_accounts_dict
    ):
        accounts = open_accounts_dict
        username = "testusername55"
        password = "testpassword354"
        result = login_into_acc(username=username, password=password, accounts=accounts)
        assert result is True

    def test_login_into_acc_return_false_if_username_not_valid(
        self, open_accounts_dict
    ):
        accounts = open_accounts_dict
        username = "123"
        password = "testpassword354"
        result = login_into_acc(username=username, password=password, accounts=accounts)
        assert result is False

    def test_login_into_acc_return_false_if_password_not_valid(
        self, open_accounts_dict
    ):
        accounts = open_accounts_dict
        username = "testusername55"
        password = "123"
        result = login_into_acc(username=username, password=password, accounts=accounts)
        assert result is False

    def test_login_into_acc_return_false_if_username_and_password_not_valid(
        self, open_accounts_dict
    ):
        accounts = open_accounts_dict
        username = "123"
        password = "123"
        result = login_into_acc(username=username, password=password, accounts=accounts)
        assert result is False


class TestRegisterManagement:
    def test_register_acc_return_account_data_and_message_if_username_login_password_are_valid(
        self, open_accounts_dict
    ):
        accounts = open_accounts_dict
        username = "testusername44"
        login = "testlogin21"
        password = "testpassword453"
        result, message = register_acc(
            username=username, login=login, password=password, accounts=accounts
        )
        assert message == "Account registered."
        assert username in accounts
        assert accounts[username]["login"] == login
        assert accounts[username]["password"] == password
        assert accounts[username]["token"] is not None

    def test_register_acc_return_false_and_error_message_if_username_invalid(
        self, open_accounts_dict
    ):
        accounts = open_accounts_dict
        username = "1"
        login = "testlogin21"
        password = "testpassword453"
        result, message = register_acc(
            username=username, login=login, password=password, accounts=accounts
        )
        assert result is False
        assert "Invalid username" in message
        assert username not in accounts

    def test_register_acc_return_false_and_error_message_if_login_invalid(
        self, open_accounts_dict
    ):
        accounts = open_accounts_dict
        username = "testusername44"
        login = "1"
        password = "testpassword453"
        result, message = register_acc(
            username=username, login=login, password=password, accounts=accounts
        )
        assert result is False
        assert "Invalid login" in message
        assert username not in accounts

    def test_register_acc_return_false_and_error_message_if_password_invalid(
        self, open_accounts_dict
    ):
        accounts = open_accounts_dict
        username = "testusername44"
        login = "testlogin21"
        password = "1"
        result, message = register_acc(
            username=username, login=login, password=password, accounts=accounts
        )
        assert result is False
        assert "Invalid password" in message
        assert username not in accounts
