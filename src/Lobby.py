from User import User
from Prompt import Prompt
from DallE import DallEContext
from enum import Enum

class LobbyType:
    Public = 0,
    Private = 1

class Lobby:
    def __init__(self, _lobbyType: LobbyType, _users: list[User], _dalleContext: DallEContext):
        self.users: dict[str, User] = {} 
            
        for user in _users:
            self.users[user.userID] = user

        self.lobbyType = _lobbyType        
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


