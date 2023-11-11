from User import User
from Prompt import Prompt
from DallE import DallEContext
from enum import Enum

class LobbyType(Enum):
    Public = 0,
    Private = 1
    
class Lobby:
    maxUser: int = 10

    def __init__(self, _lobbyID: str, _lobbyType: LobbyType, _users: list[User], _dalleContext: DallEContext):
        self.lobbyID = _lobbyID
        
        self.users: dict[str, User] = {} 
            
        for user in _users:
            self.users[user.userID] = user

        self.lobbyType: LobbyType = _lobbyType        
        # self.prompts: dict[str, Prompt] = {} I don't dare to delete this just in case
        self.dalleContext: DallEContext = _dalleContext
        self.dalleContext.Initialize()
        self.CurrentTurn: str = list(self.users.values())
        self.round: int = 1
        self.hasStarted: bool = False
        self.prompts: list[list] = [] # 2D list
        self.maxRound: int = -1

    def createPrompt(self, userID:  str, message: str, size: str) -> Prompt:
        prompt: Prompt = None
            
        if (not(userID in self.users.keys())):
            print(f"User with ID {userID} not found.")
            return prompt

        try: 
            result = self.dalleContext.Prompt(message, size)
            prompt = Prompt(result["created"], message, result)
            self.prompts[self.users[userID].num + round] = prompt #shifts depending on round

        except Exception as e:
            print(e)
 
        return prompt

    def addUser(self, user: User) -> bool:
        if (user.userID in self.users.keys()):
            self.users[user.userID] = user
            raise Exception(f"User with ID {user.userID} already exists.")
        elif (len(self.users) > max):
            raise Exception(f"Lobby is full.")

        self.users[user.userID] = user
        self.prompts.append([])

        return True

    # needs to be changed? now has rounds instead of turns per player
    def changeTurn(self) -> str: #def isRoundDone(self) -> bool
        # vals: list[str] = self.users.values()

        # currentTurn = 0

        # for value in self.users.values:
        #     if (value == self.CurrentTurn):
        #         break
        #     currentTurn += 1

        # currentTurn += 1
        
        # if (currentTurn >= len(self.users.values())):
        #     currentTurn = 0

        # self.CurrrentTurn = list(self.users.values)[0]

        # return self.CurrentTurn
        
        isRoundFinished: bool = len(self.prompts[self.round]) == len(self.users)
        return isRoundFinished

    def removeUser(self, userID: str) -> bool:
        try:
            del self.users[userID]

        except KeyError as e:
            print(f"User with ID {userID} does not exist.")
            return False

        return True

    def toDict(self) -> dict:
        promptDict: dict = {}
        for key in self.prompts.keys():
            promptDict[key] = self.prompts[key].toDict()

        return dict({
            "id": self.lobbyID,
            "type": self.lobbyType.value,
            "usercount": len(self.users),
            "prompts": promptDict,
        }) 

    def startGame(self):
        self.hasStarted = True
        self.maxRound = len(self.users)

