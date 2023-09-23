# Test cases: 
from LobbyManager import LobbyManager
from Lobby import Lobby, LobbyType
from User import User

def main() :
    lobbyManager = LobbyManager("") # DO NOT PUSH TO GITHUB
    lobby = lobbyManager.createLobby([User("123", "Jack")], LobbyType.Public)
    print(lobby.createPrompt("123", "air guitar", "512x512").toDict())

main()