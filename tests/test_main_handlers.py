import pytest

from management_services.main_handlers import (
    handle_user_login,
    handle_user_registration,
    handle_guess_game_actions,
    handle_get_user_records,
    handle_update_username,
    handle_update_password,
)
from management_services.read_write_users_data_functions import read_data_from_file


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


class TestMainHandlers:
    def test_handle_user_login_return_message_and_true_if_logged(
        self, open_accounts_dict
    ):
        accounts = open_accounts_dict
        username = "testusername55"
        password = "testpassword354"
        assert username in accounts
        assert accounts[username]["password"] == password
        message, result = handle_user_login(
            username=username, password=password, accounts=accounts
        )
        assert result is True
        assert message == "Logged successfully."

    def test_handle_user_login_return_message_and_false_if_login_fail(
        self, open_accounts_dict
    ):
        accounts = open_accounts_dict
        username = "1"
        password = "2"
        message, result = handle_user_login(
            username=username, password=password, accounts=accounts
        )
        assert result is False
        assert message == "Invalid login credentials."

    def test_handle_user_registration_return_message_and_populate_accounts_dict_if_account_created(
        self, open_accounts_dict
    ):
        accounts = open_accounts_dict
        username = "validuser111"
        password = "validpassword111"
        result = handle_user_registration(
            username=username, password=password, accounts=accounts
        )
        assert result == "Account registered."
        assert username in accounts
        assert accounts[username]["password"] == password

    def test_handle_user_registration_raises_error_if_registration_fails(
        self, open_accounts_dict
    ):
        accounts = open_accounts_dict
        username = "1"
        password = "1"
        with pytest.raises(ValueError) as exc_info:
            handle_user_registration(
                username=username, password=password, accounts=accounts
            )
            assert str(exc_info.value) == "Username must be in range 6-15."
            assert username not in accounts

    def test_handle_get_user_records_return_records_if_user_records_in_records_dict(
        self, open_records_dict
    ):
        records = open_records_dict
        username = "testusername55"
        assert username in records
        result = handle_get_user_records(username=username, user_records=records)
        assert isinstance(result, dict)

    def test_handle_get_user_records_return_message_if_user_records_not_found(
        self, open_records_dict
    ):
        records = open_records_dict
        username = "1"
        assert username not in records
        result = handle_get_user_records(username=username, user_records=records)
        assert result == "Personal records not found."

    def test_handle_update_username_return_message_and_update_username_if_username_valid(
        self, open_accounts_dict, open_records_dict
    ):
        accounts = open_accounts_dict
        records = open_records_dict
        username = "testusername55"
        new_username = "testusername99"
        assert username in accounts
        assert username in records
        result = handle_update_username(
            username=username,
            new_username=new_username,
            accounts=accounts,
            records=records,
        )
        assert result == f"Username changed to {new_username}."
        assert username not in accounts
        assert username not in records
        assert new_username in accounts
        assert new_username in records

    def test_handle_update_username_raise_value_error_if_username_invalid(
        self, open_accounts_dict, open_records_dict
    ):
        accounts = open_accounts_dict
        records = open_records_dict
        username = "testusername55"
        new_username = "1"
        assert username in accounts
        assert username in records
        with pytest.raises(ValueError) as exc_info:
            handle_update_username(
                username=username,
                new_username=new_username,
                accounts=accounts,
                records=records,
            )
            assert str(exc_info.value) == "Username must be in range 6-15."
            assert new_username not in accounts
            assert new_username not in records
            assert username in accounts
            assert new_username in records
