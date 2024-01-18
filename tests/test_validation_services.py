from management_services.read_write_users_data_functions import read_data_from_file
from validation_services.validate_registration import validate_username


class TestRegisterValidation:
    accounts_dict = read_data_from_file(
        filename="tests/test_data/test_accounts.json", dict_key="accounts"
    )

    def test_validate_username_return_false_if_username_too_short(self):
        username = "12345"
        result = validate_username(
            username=username, accounts_file_dct=self.accounts_dict
        )

        assert result is False

    def test_validate_username_return_false_if_username_too_long(self):
        username = "1234678912345678"
        result = validate_username(
            username=username, accounts_file_dct=self.accounts_dict
        )

        assert result is False

    def test_validate_username_return_false_if_digits_sum_in_username_too_small(self):
        username = "testusername1"
        result = validate_username(
            username=username, accounts_file_dct=self.accounts_dict
        )

        assert result is False

    def test_validate_username_return_false_if_username_in_accounts_dict(self):
        username = "testusername5555"
        result = validate_username(
            username=username, accounts_file_dct=self.accounts_dict
        )
        assert result is False
