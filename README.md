# guesses-game-HTTP

This is a basic http guessing game that includes user registration, playing, and saving the game.

## Game structure

- Requests username and password
- If there is an open game under the username, it asks whether to continue a previous game.
- Starts a game: Asks the user to guess a number. 
- Prints comparison result
- After each guess, it asks whether to exit and save or continue.
- In case of a correct guess, asks whether to continue another game or quit

## How to run

- clone the repository
- Configure and run the virtual environment
```
pip install -r req.txt
```
```
cd server
```
```
uv run fastapi dev
```
- Open new terminal

```
cd ../
```
python client.py
```