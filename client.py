import json
import questionary
from validations import is_num
from manage_api import *


def get_user_guess() -> int:

    guess = questionary.text("Enter num to guess: ", validate= is_num).ask()
    return int(guess)
            

def ask_to_restore_game() -> bool:
   
    ans = questionary.select("Do you want to continue the previous game?", choices= ["yes", "no"]).ask()
    if ans=="yes":
        return True
    else:
        return False

def ask_to_continue() -> bool:
    ans = questionary.select("DO you want to cuntinue?", choices=["yes","no"]).ask()
    if ans=="yes":
        return True
    else:
        return False

def ask_to_finish_game() -> bool:
    ans = questionary.select("Would you want to finish the game?", choices=["yes", "no"]).ask()
    if ans == "yes":
        return True
    else:
        return False
    
def run_game():

    while True:
        username = create_username()
        password = create_password()

        status_code, auth_data = signin(username, password)

        if status_code != 200:
            print(f"Error: {auth_data.get('detail', 'Login failed')}")
            continue

        resume = False
        if auth_data["hasSavedGame"]:
            resume = ask_to_restore_game()

        c, start_data = start_game(username, resume)
        print ({start_data.get('status', 'details')})

        while True:
            guess = get_user_guess()
            c, res = geussing_app(username, guess)

            result = res.get("result")
            status = res.get("status")


            if result == "win":
                print(f"\n🎉 Win! | Total attempts: {status["attempts"]} | Target: {status["target"]} | History: {status["history"]}\n")
                if ask_to_finish_game():
                    return
                start_game(username, False)
                continue
            hint = "Too high" if result == "big" else "Too low"
            print(f"{hint} | Attempts: {status}")
            
            if not ask_to_continue():
                exit_game(username, True)
                print("Game saved!")
                return

run_game()


    
    

