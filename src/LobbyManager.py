from Lobby import Lobby, LobbyType
from User import User
from DallE import DallEContext

class LobbyManager:
    def __init__(self, _apiKey: str): 
        self.lobbyMap: dict[str, Lobby]
        self.apiKey = _apiKey

    def createLobby(self, users: list[User], lobbyType: LobbyType) -> Lobby:
        return Lobby(lobbyType, users, DallEContext(self.apiKey))

    def deleteLobby(self, id: str):
        try:
            del self.lobbyMap[id]
            return True

        except KeyError as e:
            print("Key not found")
        return False

