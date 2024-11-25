# gamehub/games/tic_tac_toe.py

from games.base_game import BaseGame

class TicTacToe(BaseGame):
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def display_board(self):
        print("\n")
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print("---------")
        print("\n")

    def play(self):
        while " " in self.board:
            self.display_board()
            position = int(input(f"Player {self.current_player}, choose a position (1-9): ")) - 1
            if self.board[position] == " ":
                self.board[position] = self.current_player
                if self.check_winner():
                    self.display_board()
                    print(f"Player {self.current_player} wins!")
                    return
                self.current_player = "O" if self.current_player == "X" else "X"
            else:
                print("Position already taken! Try again.")
        self.display_board()
        print("It's a draw!")

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]               # Diagonals
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != " ":
                return True
        return False
