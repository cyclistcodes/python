import random 

def roll_dice():
    return [random.randint(1,6) for _ in range(5)]

def is_yahtzee(dice):
    # Check if all dice have the same value
    return len(set(dice)) == 1

def play_game():
    roll_count = 0

    while True:
        dice = roll_dice()
        print("Roll dice: ", dice)

        roll_count += 1
        if roll_count == 3:
            print("Game over")
            break

        choice = input("Do you want play again?: (y/n)")

        if choice != "y":
            break 

if __name__ == "__main__":
    play_game()