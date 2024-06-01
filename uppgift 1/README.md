# Yahtzee Game

This Python script simulates a simplified version of the Yahtzee game and have a test too. 

## Author 

Written by Isaac Skog

## How to Play

1. **Starting the Game**
   - Run the script `python3 yahtzee.py`.
   - Run the test `pytest`.
   
2. **Game Rules**
   - You have 3 rolls to get a Yahtzee (all dice showing the same value).
   - After each roll, the dice values will be displayed.
   - If you get a Yahtzee, the game will congratulate you and end.
   - If you do not get a Yahtzee after 3 rolls, the game will end.

3. **Playing Again**
   - After each roll (except the last one), you will be asked if you want to roll again.
   - Type `y` to roll again, or anything else to end the game.

## Functions in the Code

- `roll_dice()`: Rolls five dice and returns their values.
- `is_yahtzee(dice)`: Checks if all dice have the same value.
- `play_game()`: Main function that controls the game flow.

## How to Run

- Ensure you have Python3 installed on your system.
- Execute `python3 yahtzee.py` in your terminal or command prompt.
- Execute `pytest` in your terminal or command prompt to run the test. 