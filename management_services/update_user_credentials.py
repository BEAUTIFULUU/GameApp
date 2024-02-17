from validation_services.validate_user_credentials import (
    validate_username,
    validate_password,
)


def _update_username_in_records_dict(
    username: str, new_username: str, records_dict: dict[str, dict]
) -> None:
    records_dict[new_username] = records_dict.pop(username)


def update_username_in_acc_dict(
    username: str,
    new_username: str,
    accounts: dict[str, dict],
    records: dict[str, dict],
) -> ValueError | None:
    result = validate_username(username=new_username, accounts_file_dct=accounts)
    if result is not None:
        return result

    accounts[new_username] = accounts.pop(username)
    if username in records:
        _update_username_in_records_dict(
            username=username, new_username=new_username, records_dict=records
        )
    return None


def update_password_in_acc_dict(
    new_password: str, username: str, accounts: dict[str, dict]
) -> ValueError | None:
    result = validate_password(user_password=new_password, accounts_file_dct=accounts)
    if result is not None:
        return result

    accounts[username]["password"] = new_password
    return None
