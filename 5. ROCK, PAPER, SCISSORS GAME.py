import random

def play_round(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

def play_game():
    player_wins = 0
    computer_wins = 0

    while player_wins < 2 and computer_wins < 2:
        print("\nLet's play Rock, Paper, Scissors!")
        player_choice = user_choice()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = play_round(player_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_wins += 1
        elif result == "Computer wins!":
            computer_wins += 1

        print(f"\nPlayer: {player_wins}  Computer: {computer_wins}")

    if player_wins > computer_wins:
        print("\nCongratulations! You won the game!")
    else:
        print("\nComputer wins the game!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        play_game()
    else:
        print("Thank you for playing!")



play_game()
