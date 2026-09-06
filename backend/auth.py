def login(username, password):
    if not username or not password:
        return {"authenticated": False}

    if username == "admin" and password == "secret":
        return {"authenticated": True}

    return {"authenticated": False}
