import random

def roll_dice():
    return random.randrange(1,7)

def check_win(dice_rolls):
    for a in range(3):
        if dice_rolls[a] != dice_rolls[0]:
            return False
    return True

player1_wins = False
player2_wins = False

while not player1_wins and not player2_wins:
    player1_roll = [roll_dice(), roll_dice(), roll_dice()]
    player2_roll = [roll_dice(), roll_dice(), roll_dice()]
    
    print("Player 1 rolls:", player1_roll)
    print("Player 2 rolls:", player2_roll)
    
    if check_win(player1_roll):
        player1_wins = True
    elif check_win(player2_roll):
        player2_wins = True

if player1_wins:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
