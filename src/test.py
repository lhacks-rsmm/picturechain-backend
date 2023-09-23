# Test cases: 
from LobbyManager import LobbyManager
from Lobby import Lobby
from User import User

def main() :
    lobbyManager = LobbyManager("") # DO NOT PUSH TO GITHUB
    lobby = lobbyManager.createLobby([User("123", "Jack")])
    print(lobby.createPrompt("123", "air guitar", "512x512"))

main()