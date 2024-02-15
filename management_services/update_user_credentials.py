from typing import Tuple

from validation_services.validate_credentials_to_update import validate_new_username


def update_username_in_acc_dict(
    username: str, new_username: str, accounts: dict[str, dict]
) -> Tuple[bool, str] | Tuple[bool, str]:
    login = accounts[username].get("login")
    username_result = validate_new_username(
        new_username=new_username, login=login, accounts=accounts
    )
    if username_result is not None:
        return False, username_result

    accounts[new_username] = accounts.pop(username)
    return True, "Username changed."
