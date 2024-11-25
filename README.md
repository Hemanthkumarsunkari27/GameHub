# GameHub

**GameHub** is a Python project that acts as a hub for multiple mini-games. The project uses modular Object-Oriented Programming (OOP) to create scalable, stable, and easily testable game modules.

## Games Included

1. **General Knowledge Quiz** - Test your general knowledge with a series of questions.
2. **Tic Tac Toe** - Play the classic game against a friend or an AI.
3. **Hangman** - Guess the word letter-by-letter before you run out of attempts.
4. **Anagram** - Unscramble letters to find the correct word.
5. **Solver** - Solve math or word problems with hints.

## Project Structure

gamehub/ ├── games/ │ ├── gk_quiz.py │ ├── tic_tac_toe.py │ ├── hangman.py │ ├── anagram.py │ └── solver.py ├── tests/ │ ├── test_gk_quiz.py │ ├── test_tic_tac_toe.py │ ├── test_hangman.py │ ├── test_anagram.py │ └── test_solver.py └── main.py



- **main.py**: The main hub file that allows users to select and play games.
- **games/**: Contains modules for each individual game.
- **tests/**: Contains unit tests for each game module to ensure functionality.

## Installation

Install required packages:
pip install -r requirements.txt


### Usage
Run main.py to access the GameHub:
python main.py


#### Running Tests
You can run all tests by executing:
python -m unittest discover -s tests
