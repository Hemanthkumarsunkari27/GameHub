# tests/test_tic_tac_toe.py

import unittest
from games.tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        # Initialize a TicTacToe game before each test
        self.game = TicTacToe()

    def test_initial_board(self):
        # Test that the board is empty at the start
        empty_board = [['' for _ in range(3)] for _ in range(3)]
        self.assertEqual(self.game.board, empty_board, "Initial board should be empty")

    def test_make_move(self):
        # Test making a valid move
        result = self.game.make_move(0, 0, 'X')
        self.assertTrue(result, "Valid move should return True")
        self.assertEqual(self.game.board[0][0], 'X', "Board should reflect the move")

    def test_check_winner(self):
        # Simulate a winning condition and test
        self.game.board = [
            ['X', 'X', 'X'],
            ['', '', ''],
            ['', '', '']
        ]
        winner = self.game.check_winner()
        self.assertEqual(winner, 'X', "X should be detected as the winner")

if __name__ == '__main__':
    unittest.main()
