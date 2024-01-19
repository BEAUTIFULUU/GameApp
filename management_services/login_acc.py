def login_into_acc(username: str, password: str, accounts: dict) -> bool:
    if username in accounts.keys() and password == accounts[username]["password"]:
        return True

    return False
