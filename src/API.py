import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from User import User
from typing import Annotated 
from Lobby import LobbyType
from LobbyManager import LobbyManager
import json
app = FastAPI()

# origins = [
#     "*"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

class LobbyModel(BaseModel):
    userID: str
    lobbyType: int

class JoinModel(BaseModel):
    lobbyID: str
    userID: str

class PromptModel(BaseModel):
    lobbyID: str
    userID: str
    message: str


lobbyManager = LobbyManager(os.environ["OPENAI_KEY"]) 

async def getLobbyManager():
    return lobbyManager 

@app.post("/createLobby")
async def createLobby(lobbyModel: LobbyModel, _lobbyManager: Annotated[LobbyManager, Depends(getLobbyManager)]):
    t = LobbyType.Public
    if (lobbyModel.lobbyType == 1):
        t = LobbyType.Private
    return _lobbyManager.createLobby([User(lobbyModel.userID, "")], t).toDict()

@app.post("/joinLobby")
async def joinLobby(joinModel: JoinModel, _lobbyManager: Annotated[LobbyManager, Depends(getLobbyManager)]):
    try:
        _lobbyManager.lobbyMap[joinModel.lobbyID].addUser(User(joinModel.userID, ""))
    except KeyError:
        raise HTTPException(status_code=500, detail=f"Lobby {joinModel.lobbyID} does not exist.")
    except:
        return {"error": "User already exists"}

@app.post("/prompt")
async def createPrompt(promptModel: PromptModel, _lobbyManager: Annotated[LobbyManager, Depends(getLobbyManager)]):
    try:
        return _lobbyManager.lobbyMap[promptModel.lobbyID].createPrompt(promptModel.userID, promptModel.message, "512x512")
    except KeyError:
        raise HTTPException(status_code=500, detail=f"Lobby {promptModel.lobbyID} does not exist.")

@app.get("/changeTurn/{lobbyID}")
async def changeTurn(lobbyID: str, _lobbyManager: Annotated[LobbyManager, Depends(getLobbyManager)]):
    turn: str = None
    try:
        turn = _lobbyManager.lobbyMap[lobbyID].changeTurn()
    except KeyError:
        return {"error": f"Lobby {lobbyID} does not exist."} 
    return turn

@app.get("/getLobbies")
async def getLobbies(_lobbyManager: Annotated[LobbyManager, Depends(getLobbyManager)]):
    return _lobbyManager.ListLobbiesDict()

@app.get("/getLobby/{lobbyID}")
async def getLobby(lobbyID: str, _lobbyManager: Annotated[LobbyManager, Depends(getLobbyManager)]):
    try:
        return _lobbyManager.lobbyMap[lobbyID].toDict()
    except KeyError:
        raise HTTPException(status_code=500, detail=f"Lobby {lobbyID} does not exist.")
    

 
