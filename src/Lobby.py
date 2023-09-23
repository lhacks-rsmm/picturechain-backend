from User import User
from Prompt import Prompt
from DallE import DallEContext
from enum import Enum

class LobbyType():
    Public = 0,
    Private = 1

class Lobby:
    def __init__(self, _lobbyID: str, _lobbyType: LobbyType, _users: list[User], _dalleContext: DallEContext):
        self.lobbyID = _lobbyID
        
        self.users: dict[str, User] = {} 
            
        for user in _users:
            self.users[user.userID] = user

        self.lobbyType: LobbyType = _lobbyType        
        self.prompts: dict[str, Prompt] = {}
        self.dalleContext = _dalleContext
        self.dalleContext.Initialize()

    def createPrompt(self, userID:  str, message: str, size: str) -> Prompt:
        prompt: Prompt = None
        if (not(userID in self.users.keys())):
            print(f"User with ID {userID} not found.")
            return prompt

        try: 
            result = self.dalleContext.Prompt(message, size)
            prompt = Prompt(result["created"], message, result)
            self.prompts[prompt.promptID] = prompt

        except Exception as e:
            print(e)
 
        return prompt

    def addUser(self, user: User) -> bool:
        if (user.userID in self.users.keys()):
            self.users[user.userID] = user
            raise Exception(f"User with ID {user.userID} already exists.")

        self.users[user.userID] = user

        return True

    def removeUser(self, userID: str) -> bool:
        try:
            del self.users[userID]

        except KeyError as e:
            print(f"User with ID {userID} does not exist.")
            return False

        return True

    def toDict(self):
        promptDict: dict = {}
        for key in self.prompts.keys():
            promptDict[key] = self.prompts[key].toDict()


        return dict({
            "id": self.lobbyID,
            "type": str(self.lobbyType[0]),
            "prompts": promptDict,
        }) 


