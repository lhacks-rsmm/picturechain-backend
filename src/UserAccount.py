from User import User

class UserAccount:
    def __init__(self, _user: User, _passwordHash: str):
        self.user = _user
        self.passwordHash = _passwordHash
