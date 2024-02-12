import pytest
from management_services.read_write_users_data_functions import read_data_from_file
from validation_services.validate_registration import (
    validate_username,
    validate_login,
    validate_password,
)


@pytest.fixture
def open_accounts_dict():
    accounts_dict = read_data_from_file(
        filename="tests/test_data/test_accounts.json", dict_key="accounts"
    )
    return accounts_dict


class TestRegisterValidation:
    def test_validate_username_return_none_if_username_valid(self, open_accounts_dict):
        accounts_dict = open_accounts_dict
        username = "valusername333"
        result = validate_username(username=username, accounts_file_dct=accounts_dict)
        assert result is None

    def test_validate_username_return_message_if_username_too_short(
        self, open_accounts_dict
    ):
        accounts_dict = open_accounts_dict
        username = "12345"
        result = validate_username(username=username, accounts_file_dct=accounts_dict)

        assert result == "Username must be in range (6-15)"

    def test_validate_username_return_message_if_username_too_long(
        self, open_accounts_dict
    ):
        accounts_dict = open_accounts_dict
        username = "1234678912345678"
        result = validate_username(username=username, accounts_file_dct=accounts_dict)

        assert result == "Username must be in range (6-15)"

    def test_validate_username_return_message_if_digits_sum_in_username_too_small(
        self, open_accounts_dict
    ):
        accounts_dict = open_accounts_dict
        username = "testusername1"
        result = validate_username(username=username, accounts_file_dct=accounts_dict)

        assert result == "Username must have at least 3 digits."

    def test_validate_username_return_message_if_username_in_accounts_dict(
        self, open_accounts_dict
    ):
        accounts_dict = open_accounts_dict
        username = "testusername55"
        result = validate_username(username=username, accounts_file_dct=accounts_dict)
        assert result == "Username already exists."

    def test_validate_login_return_none_if_login_valid(self, open_accounts_dict):
        accounts_dict = open_accounts_dict
        login = "validlogin1"
        result = validate_login(
            user_login=login, username="1234", accounts_file_dct=accounts_dict
        )
        assert result is None

    def test_validate_login_return_message_if_login_too_short(self, open_accounts_dict):
        accounts_dict = open_accounts_dict
        login = "12345"
        result = validate_login(
            user_login=login, username="54321", accounts_file_dct=accounts_dict
        )
        assert result == "Login needs to be in range (6-15)"

    def test_validate_login_return_message_if_login_too_long(self, open_accounts_dict):
        accounts_dict = open_accounts_dict
        login = "1234567891234567889"
        result = validate_login(
            user_login=login, username="54321", accounts_file_dct=accounts_dict
        )
        assert result == "Login needs to be in range (6-15)"

    def test_validate_login_return_message_if_digits_sum_in_login_too_small(
        self, open_accounts_dict
    ):
        accounts_dict = open_accounts_dict
        login = "testlogin"
        result = validate_login(
            user_login=login, username="54321", accounts_file_dct=accounts_dict
        )
        assert result == "Login must have at least 1 digit."

    def test_validate_login_return_message_if_login_in_accounts_dict(
        self, open_accounts_dict
    ):
        accounts_dict = open_accounts_dict
        login = "testlogin12"
        result = validate_login(
            user_login=login, username="54321", accounts_file_dct=accounts_dict
        )
        assert result == "Login already exist."

    def test_validate_login_return_message_if_login_and_username_are_the_same(
        self, open_accounts_dict
    ):
        accounts_dict = open_accounts_dict
        login = "testlogin123"
        username = "testlogin123"
        result = validate_login(
            user_login=login, username=username, accounts_file_dct=accounts_dict
        )
        assert result == "Login needs to be different than username."

    def test_validate_password_return_none_if_password_valid(self, open_accounts_dict):
        accounts_dict = open_accounts_dict
        password = "validpassword333"
        result = validate_password(
            user_password=password, accounts_file_dct=accounts_dict
        )
        assert result is None

    def test_validate_password_return_message_if_password_too_short(
        self, open_accounts_dict
    ):
        accounts_dict = open_accounts_dict
        password = "123"
        result = validate_password(
            user_password=password, accounts_file_dct=accounts_dict
        )
        assert result == "Password needs to be in range (8-19)"

    def test_validate_password_return_message_if_password_too_long(
        self, open_accounts_dict
    ):
        accounts_dict = open_accounts_dict
        password = "12345667878989976967976"
        result = validate_password(
            user_password=password, accounts_file_dct=accounts_dict
        )
        assert result == "Password needs to be in range (8-19)"

    def test_validate_password_return_message_if_digits_sum_in_password_too_small(
        self, open_accounts_dict
    ):
        accounts_dict = open_accounts_dict
        password = "testpassword11"
        result = validate_password(
            user_password=password, accounts_file_dct=accounts_dict
        )
        assert result == "Password must have at least 3 digits."

    def test_validate_password_return_message_if_password_in_accounts_dict(
        self, open_accounts_dict
    ):
        accounts_dict = open_accounts_dict
        password = "testpassword354"
        result = validate_password(
            user_password=password, accounts_file_dct=accounts_dict
        )
        assert result == "Invalid password"
