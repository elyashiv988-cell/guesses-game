from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from auth import signin, create_user
from storge import save_game, find_corrent_username, default_saved_game
from game import compering_nums, create_random_num

app = FastAPI()

class Creds(BaseModel):
    username: str
    password: str


@app.post("/api/login")
def login(creds: Creds):
    result = signin(creds.username, creds.password)
    
    if result == "not_found":
        if create_user(creds.username, creds.password):
            return {"login": True, "hasSavedGame": False}
        else: 
            raise HTTPException(status_code=401, detail="Error! username already exists")
    elif result == "wrong_password":
        raise HTTPException(status_code=401, detail="Incorrect password!")
    elif result == "active":
        return {"login": True, "hasSavedGame": True}
    elif result == "inactive":
        return {"login": True, "hasSavedGame": False}

        
@app.get("/api/game/start")
def strat_game(username: str, resume: bool):

    user = find_corrent_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if resume:
        
        if user["saved_game"]["isActive"] == True:
            return {"status": "Continues previous game", "details": {"attemps":user["saved_game"]["attempts"], "history": user["saved_game"]["history"]}}
        else:
            raise HTTPException(status_code=404, detail=f"Not found saved game!")
    else:
        user["saved_game"] = default_saved_game()
        target = create_random_num(0,10)
        user["saved_game"]["target"]=target
        user["saved_game"]["isActive"]= True
        save_game(user)
        return {"status": "New game"}
    


@app.post("/api/game/guess")
def geussing_app(username, guess):
    user = find_corrent_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    target = user["saved_game"]["target"]
    user["saved_game"]["attempts"] += 1
    user["saved_game"]["history"].append(int(guess))
    save_game(user)
    
    result = compering_nums(target, int(guess))
    if result=="win":
        history = user["saved_game"] 
        user["saved_game"] = default_saved_game()
        save_game(user)
        return {"result": result, "status": history}
    return {"result": result, "status": user["saved_game"]["attempts"]}

@app.post("/api/game/exit")
def exit_game(username: str, save: bool):
    user = find_corrent_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not save:
        user["saved_game"] = default_saved_game()
        save_game(user)
    
    return {"status": "exited"}
    
