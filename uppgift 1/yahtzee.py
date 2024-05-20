import random

class YahtzeeGame:
    def __init__(self):
        self.dice = [random.randint(1,6) for _ in range(5)]
        self.roll_count=0

    def roll_dice(self):
        self.dice = [random.randint(1,6) for _ in range(5)]