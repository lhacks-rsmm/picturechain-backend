# picturechain-backend
Backend for picture chain

## Python Dependencies
`pip install fastapi[all] pydantic openai`

## Running the server
`cd src`
`uvicorn API:app --reload`


## API Endpoints

* /createLobby
    Creates a lobby with a user
    Method: POST
    Headers: 
        Content-Type: application/json 

    Model: {
            "userID": string,
            "lobbyType": int 
        }

* /joinLoby
    Adds the given user to the given lobby
    Method: POST
    Headers: 
        Content-Type: application/json 

    Model: {
            "userID": string,
            "lobbyID": string 
        }

* /prompt
    Creates a prompt
    Method: POST
    Headers: 
        Content-Type: application/json 

    Model: {
            "lobbyID": string,
            "userID": string,
            "message": string
        }

* /getLobby/{lobbyID} 
    Returns the state of the given lobby.
    Method: GET

    Params:
        lobbyID: int