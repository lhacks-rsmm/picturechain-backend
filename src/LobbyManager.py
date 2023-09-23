from Lobby import Lobby, LobbyType
from User import User
from DallE import DallEContext
import uuid

class LobbyManager:
    def __init__(self, _apiKey: str): 
        self.lobbyMap: dict[str, Lobby] = {}
        self.apiKey = _apiKey

    def createLobby(self, users: list[User], lobbyType: LobbyType) -> Lobby:
        lobby = Lobby(str(uuid.uuid4()), lobbyType, users, DallEContext(self.apiKey))

        self.lobbyMap[lobby.lobbyID] = lobby

        return lobby

    def deleteLobby(self, id: str) -> bool:
        try:
            del self.lobbyMap[id]
            return True

        except KeyError as e:
            print("Key not found")

        return False
    
    def ListLobbies(self) -> list[Lobby]:
        lobbies: list = []

        for key in self.lobbyMap.keys():
            lobbies.append(self.lobbyMap[key])

        return lobbies
    
    def ListLobbiesDict(self) -> list[Lobby]:
        lobbies: list = []

        for key in self.lobbyMap.keys():
            lobbies.append(self.lobbyMap[key].toDict())

        return lobbies

