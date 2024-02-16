from validation_services.validate_credentials_to_update import validate_new_username


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
    login = accounts[username].get("login")
    result = validate_new_username(
        new_username=new_username, login=login, accounts=accounts
    )
    if result is not None:
        return result

    accounts[new_username] = accounts.pop(username)
    _update_username_in_records_dict(
        username=username, new_username=new_username, records_dict=records
    )
    return None
