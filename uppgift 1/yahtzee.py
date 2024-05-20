import random

class YahtzeeGame:
    def __init__(self):
        self.dice = [random.randint(1,6) for _ in range(5)]
        self.roll_count=0

    def roll_dice(self):
        self.dice = [random.randint(1,6) for _ in range(5)]

    def print_dice(self):
        print("Dice roll: ",self.dice)

    def is_yahtzee(self):
        return all(die == self.dice[0] for die in self.dice)