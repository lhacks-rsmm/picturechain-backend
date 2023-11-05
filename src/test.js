import fetch from "node-fetch";


let url = "http://127.0.0.1:8000";
let lobbyID = "551c73f5-1b84-4e59-baa3-b097c5149fee";

async function createLobby(id, type)
{
    var response = await fetch(url + "/createLobby", {
        method: "POST",
        body: JSON.stringify({
            userID: id,
            lobbyType: type
        }),
        headers: {
            "Content-Type": "application/json"
        },
        mode: "cors" // makes sure that the server only allow certain clients to make requests, and will only respond to clients in its list
    });

    return await response.json();
}

// var lobby = await createLobby("zongxina", 0);

async function createPrompt(_lobbyID, _userID, _message) {
    let response = await fetch(url + "/prompt", {
        method: "POST",
        body: JSON.stringify({
            lobbyID: _lobbyID,
            userID: _userID,
            message: _message
        }),
        headers: {
            "Content-Type" : "application/json"
        },
        mode: "cors"
    });

    return await response.json();
}

async function joinLobby(_userID, _lobbyID) {
    let response = await fetch(url + "/joinLobby", {
        method: "POST",
        body: JSON.stringify ({
            userID: _userID,
            lobbyID: _lobbyID
        }),
        headers: {
            "Content-Type": "application/json"
        },
        mode: "cors"
    });

    return await response.json();
}

async function getLobby() {
    let response = await fetch(url + "/getLobby/" + lobbyID, {
        method: "GET",
        headers : {
            "Content-Type": "application/json"
        },
        mode: "cors"
    });

    return await response.json();
}

// let lobby = await getLobby();

// console.log(lobbyStatus);

// console.log(lobby);

// let prompt = await createPrompt("551c73f5-1b84-4e59-baa3-b097c5149fee", "zongxina", "japan")

// console.log(prompt.result.data);

// console.log(lobby);

let lobbyStatus = await joinLobby("hardeepsingh", "551c73f5-1b84-4e59-baa3-b097c5149fee");
console.log(lobbyStatus);