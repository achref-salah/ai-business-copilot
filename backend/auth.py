def login(username, password):
    if username == "admin" and password == "secret":
        return {"authenticated": True}

    return {"authenticated": False}
