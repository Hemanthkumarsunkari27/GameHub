# main.py

from games.gk_quiz import GKQuiz
from games.tic_tac_toe import TicTacToe
from games.hangman import Hangman
from games.anagram import Anagram
from games.solver import Solver

def main():
    games = {
        "1": GKQuiz({"What is the capital of France?": "Paris", "What is 2 + 2?": "4"}),
        "2": TicTacToe(),
        "3": Hangman("python"),
        "4": Anagram(["python", "hangman", "tic tac toe"]),
        "5": Solver("3 + 2 * 2")
    }

    while True:
        print("Welcome to GameHub!")
        print("Select a game:")
        print("1. GK Quiz")
        print("2. Tic Tac Toe")
        print("3. Hangman")
        print("4. Anagram")
        print("5. Solver")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "6":
            print("Goodbye!")
            break
        elif choice in games:
            games[choice].play()
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
