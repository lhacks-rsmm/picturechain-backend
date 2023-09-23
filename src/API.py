import os
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from User import User
from typing import Annotated 
from Lobby import LobbyType
from LobbyManager import LobbyManager

app = FastAPI()

class LobbyModel(BaseModel):
    userID: str
    lobbyType: int

class PromptModel(BaseModel):
    lobbyID: str
    userID: str
    message: str


lobbyManager = LobbyManager(os.environ["OPENAI_KEY"]) 

async def getLobbyManager():
    return lobbyManager 

@app.post("/createLobby")
async def createLobby(lobbyModel: LobbyModel, _lobbyManager: Annotated[LobbyManager, Depends(getLobbyManager)]):
    return _lobbyManager.createLobby([User(lobbyModel.userID, "")], LobbyType(lobbyModel.lobbyType))

@app.post("/prompt")
async def createPrompt(promptModel: PromptModel, _lobbyManager: Annotated[LobbyManager, Depends(getLobbyManager)]):
    try:
        return _lobbyManager.lobbyMap[promptModel.lobbyID].createPrompt(promptModel.userID, promptModel.message, "512x512")
    except KeyError:
        raise HTTPException(status_code=500, detail=f"Lobby {promptModel.lobbyID} does not exist.")

@app.get("/getLobby/{lobbyID}")
async def getLobby(lobbyID: str, _lobbyManager: Annotated[LobbyManager, Depends(getLobbyManager)]):
    try:
        return _lobbyManager.lobbyMap[lobbyID].toDict()
    except KeyError:
        raise HTTPException(status_code=500, detail=f"Lobby {promptModel.lobbyID} does not exist.")

