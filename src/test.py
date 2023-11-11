# Test cases: 
from LobbyManager import LobbyManager
from Lobby import Lobby, LobbyType
from User import User
import os
import sys

def main() :
    URL = 'http://127.0.0.1:8000'
    # endpoints : /getLobby, /joinLobby, etc
    # GET, POST
    




    # SIZE = "512x512"
    # lobbyManager = LobbyManager(os.environ["OPENAIKEY"])     
    # lobby = lobbyManager.createLobby([User("123", "Jack"), User("abc", "Tom"), User("12c", "Pops")], LobbyType.Private)
    # print(lobby.createPrompt("abc", sys.argv[1], SIZE).result)
    # lobby.createPrompt("123", "deus ex machina", SIZE)
    # lobby.createPrompt("12c", "UI Paint App", SIZE)
    # print(lobby.addUser(User("$$$", "Money")))
    # print(lobby.addUser(User("$$$", "Money")))
    # print(lobby.removeUser("123"))
    # print(lobby.removeUser("123"))

    
# def createLobbyTest():
#     URL = "https://630a-209-87-29-242.ngrok-free.app/createLobby"
#     header = {
        
#         "Content-Type": "application/json" 
#     }

#     prompt = {
#         "userID": "123",
#         "lobbyType": LobbyType.Public.value
#     }

#     promptJson = json.dumps(prompt)
#     response = requests.post(URL, headers=header, data=promptJson)

#     print(response)
#     if int(response.status_code / 100) != 2:
#         return True
#     return False

# def joinLobbyTest():
#     URL = "https://630a-209-87-29-242.ngrok-free.app/joinLobby"
#     header = {
#         "Content-Type": application/json
#     }

#     prompt = {
#         "userID": "123",
#         "lobbyID": "abc"
#     }

#     promptJson = json.dumps(prompt)
#     response = requests.post(URL, headers=header, data=promptJson)

#     print(response)
#     if int(response.status_code / 100) != 2:
#         return True
#     return False

# def promptTest():
#     URL = "https://630a-209-87-29-242.ngrok-free.app/prompt"

# if createLobbyTest():
#     print("Create Lobby: OK!")
# else
#     print("Create Lobby: ERROR")
# if joinLobbyTest():
#     print("Join Lobby: OK!")
# else
#     print("Join Lobby: ERROR")

main()

