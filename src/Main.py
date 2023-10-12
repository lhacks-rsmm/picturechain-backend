import os
import sys
from LobbyManager import LobbyManager
from Prompt import Prompt
from User import User
import requests

lobbyManager = LobbyManager(os.environ["OpenAI_KEY"])

apiURL = ""

def createLobby(username: str):
    r = requests.post(f"{apiURL}/createLobby", headers={"Content-Type": "application/json"})

def Main():
    lobbies = requests.get(f"{apiURL}/getLobbies").json()
    
    if (len(lobbies) < 1):
        print("No lobbies exist, enter your username below to create one.")
    else:
        print(lobbies)

    username = input("Enter your username")

    while (True):
        choice = input("> ")
        if (choice == "create"):
            createLobby()



    return

Main()