class User:
    def __init__(self, _userID: str, _name: str):
        self.userID: str = _userID
        self.name: str = _name
        self.inLobby: bool = False
