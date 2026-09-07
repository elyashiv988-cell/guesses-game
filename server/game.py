import random

def create_random_num(start,end) ->int:
    num=random.randint(start,end)
    return num

def compering_nums(target,guess) -> bool:
    if guess == target:
        return "win"
    
    elif guess<target:
        print("Too small, try agein!")
        return "small"
    
    elif guess>target:
        print("Too big, try agein!")
        return "big"

