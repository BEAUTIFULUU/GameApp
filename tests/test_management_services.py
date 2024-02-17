import pytest
from management_services.read_write_users_data_functions import read_data_from_file
from management_services.game_records_management import (
    get_user_game_records,
    update_game_record,
)
from management_services.login_acc import login_into_acc
from management_services.register_acc import register_acc
from management_services.update_user_credentials import update_username_in_acc_dict


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
        password = "testpassword453"
        result = register_acc(username=username, password=password, accounts=accounts)
        assert isinstance(result, dict)
        assert username in accounts
        assert accounts[username]["password"] == password
        assert accounts[username]["token"] is not None

    def test_register_acc_return_false_and_error_message_if_username_invalid(
        self, open_accounts_dict
    ):
        accounts = open_accounts_dict
        username = "l1"
        password = "testpassword453"
        with pytest.raises(ValueError) as exc_info:
            register_acc(username=username, password=password, accounts=accounts)
            assert str(exc_info.value) == "Username must be in range 6-15."
        assert username not in accounts

    def test_register_acc_return_false_and_error_message_if_password_invalid(
        self, open_accounts_dict
    ):
        accounts = open_accounts_dict
        username = "testusername44"
        password = "1"
        with pytest.raises(ValueError) as exc_info:
            register_acc(username=username, password=password, accounts=accounts)
            assert str(exc_info.value) == "Password must be in range 8-19."
        assert username not in accounts


class TestUpdateCredentialsManagement:
    def test_update_username_in_acc_dict_return_true_and_message_if_username_valid(
        self, open_accounts_dict, open_records_dict
    ):
        accounts = open_accounts_dict
        records = open_records_dict
        username = "testusername55"
        new_username = "testusername66"
        assert username in accounts
        result = update_username_in_acc_dict(
            username=username,
            new_username=new_username,
            accounts=accounts,
            records=records,
        )
        assert result is None
        assert new_username in accounts
        assert username not in accounts

    def test_update_username_in_acc_dict_return_false_and_message_if_username_is_invalid(
        self, open_accounts_dict, open_records_dict
    ):
        accounts = open_accounts_dict
        records = open_records_dict
        username = "testusername55"
        new_username = "1"
        assert username in accounts
        with pytest.raises(ValueError) as exc_info:
            update_username_in_acc_dict(
                username=username,
                new_username=new_username,
                accounts=accounts,
                records=records,
            )
            assert str(exc_info.value) == "Username must be in range 6-15."

        assert new_username not in accounts
        assert username in accounts
