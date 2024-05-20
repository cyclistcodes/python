import random 

def roll_dice():
    return [random.randint(1,6) for _ in range]

def is_yahtzee(dice):
    return len(set(dice)) == 1