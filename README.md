# Game of Greed

Game of Greed is a dice game implemented in Python. The code demonstrates several key skills:

- **User Input**: Gets number of players from user with input validation
- **Randomness**: Simulates dice rolls using the random module
- **Control Flow**: Implements game loop and turn logic with functions 
- **Data Structures**: Uses Python lists to store player scores
- **Modularity**: Separates game logic into reusable functions
- **Parameters**: Passes data between functions using parameters
- **Returns**: Functions return values instead of relying on side effects 
- **Print Output**: Provides game status updates and instructions with print
- **Docstrings**: Contains documentation strings to explain functions
- **Readability**: Uses good naming, spacing, and code organization
- **Encapsulation**: Main function encapsulates overall game logic
- **Game Logic**: Implements essential game rules and winning conditions
- **Effective**: Clear, concise implementation of a playable game

The code demonstrates skills in:

- User interaction, print output
- Utilizing core Python features  
- Writing modular, encapsulated code
- Implementing game logic and control flow
- Documentation and readability
- Developing an effective game program

Overall, it showcases strong Python skills by implementing a fully playable dice game.
> It serves as a coding demonstration, showcasing problem-solving skills and knowledge.

## Overview

Game of Greed is a dice game for 2-4 players. Each player takes turns rolling a six-sided die and accumulating points based on the numbers rolled. The first player to reach a certain score threshold (e.g. 50 points) wins the game.

This implementation of the game is written in Python.
Uses the `random` module for simulating dice rolls. 

## Getting Started

1. Clone the repository:
```
git clone https://codeberg.org/zennon/Game-of-Greed.git
```

2.  Run the game
```
python game.py
```


## How to Play

> The "Game of Greed" is a dice game where players take turns rolling a six-sided dice.
> The objective is to accumulate the highest score possible without rolling a one. 

### Rules

- Can be played with 2 to 4 players
- Each player rolls 1 to 6 dice per turn
- Rolling a 1 loses all points for the turn
- Can roll multiple times per turn and accumulate score
- Can end turn ("bank") to add score to total
- First to reach 50 points wins

## Code Explanation

The code is written in Python and consists of the following components:

### Constants

`game.py` file contains the following constant values:

- `MIN_VALUE` and `MAX_VALUE` define the minimum and maximum values of the six-sided die.
- `MIN_PLAYERS` and `MAX_PLAYERS` define the minimum and maximum number of players allowed in the game.
- `MAX_SCORE` defines the maximum score required to end the game.

### Functions

`game.py` file contains the following functions:

- `roll()`: Simulates rolling a six-sided die and returns a random number between 1 and 6.
- `get_num_players()`: Asks the user to enter the number of players and returns the valid input.
- `handle_turn(player_idx, player_scores)`: Manages a player's turn and updating their score.
- `is_game_over(player_scores)`: Checks if the game has ended.
- `announce_winner(player_scores)`: Prints the winner of the game based on the highest score.
- `main()`: The main function that runs the game, interacting with the players and managing the game flow.

> The code utilizes functions, loops, lists, input validation, and other core Python concepts. Comments are included to explain logic and flow.

## Running the Game

Play to "Game of Greed":
1. Run `python game.py`
2. Enter number of players
3. Each player takes turns rolling the dice and accumulating their score.
4. Player reaches or exceeds the maximum score (50).
5. The game ends, and the winner with the highest score is announced.

## Origin and Contribution

### Credits

- Inspired by a tutorial by Tech With Tim

The original tutorial this code is based on is by "Tech With Tim" and can be found here: [link](https://youtu.be/21FnnGKSRZo?t=142)

### Contributing

Feel free to modify the code, make improvements, or add additional features to enhance the game further.

Contributions welcome! Some ideas:

- Add new features
- Improve game logic
- Enhance user experience
- Fix bugs
- Improve documentation

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Have fun playing the "Game of Greed"!