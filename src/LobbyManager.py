from Lobby import Lobby
from User import User

class LobbyManager:
    def __init__(self):
        self.lobbyMap: dict[str, Lobby]

    def createLobby(self, users: list[User]):
        return Lobby(users)

    def deleteLobby(self, id: str):    
        try:
            del self.lobbyMap[id]
            return True
        except KeyError as e:
            print("Key not found")
        return False

