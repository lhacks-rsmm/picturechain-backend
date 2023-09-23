from User import User

class Lobby:
    def __init__(self, users: list[User]):
        self.users = users 
        self.promptOutputs = {} # temp
        self.promptInputs = {} # temp
