from Lobby import Lobby
from User import User

class LobbyManager:
    def __init__(self):
        self.lobbyMap: dict[str, Lobby]

    def createLobby(users: list[User]):
        return Lobby(users)

    def deleteLobby(id):
        