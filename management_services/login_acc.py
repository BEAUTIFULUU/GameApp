def login_into_acc(username: str, password: str, accounts: dict):
    return username in accounts.keys() and password == accounts[username]["password"]
