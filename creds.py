import questionary

def create_password() -> str:
    
    password = questionary.text("Enter your password: ").ask()
    return password

def create_username():
    username = questionary.text("Enter username:").ask()
    return username