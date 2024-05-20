import random 

def roll_dice():
    return [random.randint(1,6) for _ in range]

def is_yahtzee(dice):
    return len(set(dice)) == 1

def play_game():
    roll_count = 0

    while True:
        dice = roll_dice()