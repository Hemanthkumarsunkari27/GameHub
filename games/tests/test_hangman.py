# tests/test_hangman.py

import unittest
from games.hangman import Hangman

class TestHangman(unittest.TestCase):

    def setUp(self):
        self.hangman = Hangman()
        self.hangman.word = "testing"  # Set a test word

    def test_get_word(self):
        word = self.hangman.get_word()
        self.assertIsInstance(word, str, "The word should be a string")

    def test_guess_letter_correct(self):
        # Test a correct guess
        result = self.hangman.guess_letter('t')
        self.assertTrue(result, "Correct guess should return True")

    def test_guess_letter_incorrect(self):
        # Test an incorrect guess
        result = self.hangman.guess_letter('z')
        self.assertFalse(result, "Incorrect guess should return False")

    def test_is_game_over(self):
        # Simulate a game-over condition
        self.hangman.remaining_attempts = 0
        self.assertTrue(self.hangman.is_game_over(), "Game should be over when attempts are zero")

if __name__ == '__main__':
    unittest.main()
