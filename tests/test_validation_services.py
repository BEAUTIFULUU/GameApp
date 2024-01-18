import pytest
from validation_services.validate_login import validate_login_credentials
from management_services.read_write_users_data_functions import read_data_from_file


def test_validate_login_credentials_return_false_if_username_too_short():
    username = "12345"
    password = "12345678"

    result = validate_login_credentials(username=username, password=password)

    assert result is False


def test_validate_login_credentials_return_false_if_password_too_short():
    username = "123456"
    password = "123"

    result = validate_login_credentials(username=username, password=password)

    assert result is False
