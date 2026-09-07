import bcrypt
from storge import save_game, stored_data, default_saved_game


def hashing_pass(password):

    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

def verify_pass(user_password, stored_hash):
    password_bytes = user_password.encode('utf-8')
    stored_hash_bytes = stored_hash.encode('utf-8')
 
    return bcrypt.checkpw(password_bytes, stored_hash_bytes)


def signin(username, password):
    for user in stored_data():
        if user["username"] == username:
            if verify_pass(password, user["password"]):
                return "active" if user["saved_game"]["isActive"] else "inactive"
            else:
                return "wrong_password"
    return "not_found"

def create_user(username, password):
    new_user = {
        "username": username,
        "password": hashing_pass(password),
        "saved_game": default_saved_game()
        }
    
    for user in stored_data():
        if user["username"] == username:
            return False
    save_game(new_user)
    return True
        
            