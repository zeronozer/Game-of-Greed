"""
Game of Greed code is based on one of the projects presented in a tutorial video, which you can find at the following link: https://youtu.be/21FnnGKSRZo. ↗
I have implemented the project in my own way, with modifications and improvements.
The purpose of this code is to showcase my skills and knowledge in Python programming, and to provide an example of how I approach coding challenges.
"""

import random

# Constants for the game
MIN_VALUE = 1
MAX_VALUE = 6
MIN_PLAYERS = 2
MAX_PLAYERS = 4
MAX_SCORE = 50

def roll() -> int:
    """
    Simulate rolling a 6-sided die.

    Returns:
        int: Random number between 1 and 6.
    """

    # Use the random.randint function to simulate a die roll.
    return random.randint(MIN_VALUE, MAX_VALUE)

def get_num_players() -> int:
    """
    Get the number of players for the game.

    Returns:
        int: Number of players.
    """

    # Start an infinite loop to get player input.
    while True:
        players = input("Enter the number of players (2-4): ")

        # Check if the input is a digit.
        if players.isdigit():
            # Convert the string input to an integer.
            players = int(players)
            # Check if the number of players is between 2 to 4.
            if MIN_PLAYERS <= players <= MAX_PLAYERS:
                return players
            else:
                print(f"Must be between {MIN_PLAYERS} - {MAX_PLAYERS} players.")
        else:
            print("Invalid, try again.")

def handle_turn(player_idx: int, player_scores: list[int]) -> None:
    """
    Handle a single player's turn.

    Args:
        player_idx (int): Index of the current player.
        player_scores (list[int]): List of scores for all players.
    """
    print(f"\nPlayer number {player_idx + 1} turn has just started!")
    print(f"Your total score is: {player_scores[player_idx]}\n")
    current_score = 0

    # Start a loop for the player's turn.
    while True:
        should_roll = input("Would you like to roll (y/n)? ")
        if should_roll.lower() != "y":
            break

        # Roll the dice.
        value = roll()
        if value == 1:
            print("You rolled a 1! Turn done!")
            current_score = 0
            break
        else:
            # Add the rolled value to the current score.
            current_score += value
            print(f"You rolled a: {value}")
            print(f"Your score is: {current_score}")

    # Add the current score to the player's total score.
    player_scores[player_idx] += current_score
    print(f"Your total score is: {player_scores[player_idx]}")

def is_game_over(player_scores: list[int]) -> bool:
    """
    Check if the game has ended.

    Args:
        player_scores (list[int]): List of scores for all players.

    Returns:
        bool: True if the game has ended, False otherwise.
    """
    return max(player_scores) >= MAX_SCORE

def announce_winner(player_scores: list[int]) -> None:
    """
    Announce the winner of the game.

    Args:
        player_scores (list[int]): List of scores for all players.
    """
    max_score = max(player_scores)
    winning_idx = player_scores.index(max_score)
    print(f"Player number {winning_idx + 1} is the winner with a score of: {max_score}")

def main() -> None:
    """
    Main function to run the game.
    """

    # Get the number of players from the user
    players = get_num_players()

    # Initialize the scores for all players to 0
    player_scores = [0 for _ in range(players)]

    # Keep playing until the game is over
    while not is_game_over(player_scores):
        # Iterate over all players
        for player_idx in range(players):
            # Handle the turn for each player
            handle_turn(player_idx, player_scores)

    # Announce the winner of the game
    announce_winner(player_scores)

if __name__ == "__main__":
    main()