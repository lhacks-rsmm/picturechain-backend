from User import User
from Prompt import Prompt
from DallE import DallEContext

class Lobby:
    def createPrompt(self, userID:  str, message: str, size: str) -> bool:
        if (not(userID in self.users.keys())):
            print(f"User with ID {userID} not found.")
            return False 

        try: 
            result = self.dalleContext.Prompt(message, size)
            prompt: Prompt = Prompt(result["created"], message, result)

        except Exception as e:
            print(e)
            return False
 
        return True 

    def __init__(self, _users: list[User], _dalleContext: DallEContext):
        self.users: dict[str, User] = {} 

        for user in _users:
            self.users[user.userID] = user
        
        self.prompts: dict[str, Prompt] = {}
        self.dalleContext = _dalleContext
