import random

def roll_dice():
    return random.randint(1, 6)

def play_round(player):
    input(f"\n{player}, Press Enter to roll the dice...")
    score = roll_dice()
    print(f"{player} rolls: {score}")
    return score

def play_game():
    player1_wins = 0
    player2_wins = 0

    while player1_wins < 2 and player2_wins < 2:
        print("\nLet's roll the dice!")
        player1_score = play_round("Player 1")
        player2_score = play_round("Player 2")

        if player1_score > player2_score:
            player1_wins += 1
            print("Player 1 wins this round!")
        elif player1_score < player2_score:
            player2_wins += 1
            print("Player 2 wins this round!")
        else:
            print("It's a tie!")

        print(f"\nPlayer 1: {player1_wins}  Player 2: {player2_wins}")

    if player1_wins > player2_wins:
        print("\nPlayer 1 wins the game!")
    else:
        print("\nPlayer 2 wins the game!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        play_game()
    else:
        print("Thank you for playing!")



play_game()

