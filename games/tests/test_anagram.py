# tests/test_anagram.py

import unittest
from games.anagram import Anagram

class TestAnagram(unittest.TestCase):

    def setUp(self):
        self.anagram = Anagram()
        self.anagram.word = "listen"  # Set a word for testing

    def test_generate_anagram(self):
        anagram_word = self.anagram.generate_anagram()
        self.assertNotEqual(anagram_word, self.anagram.word, "Anagram should not be the same as the original word")
        self.assertEqual(sorted(anagram_word), sorted(self.anagram.word), "Anagram should have the same letters as the original word")

    def test_check_anagram_correct(self):
        # Test a correct anagram solution
        result = self.anagram.check_anagram("silent")
        self.assertTrue(result, "Correct anagram should return True")

    def test_check_anagram_incorrect(self):
        # Test an incorrect anagram solution
        result = self.anagram.check_anagram("wrong")
        self.assertFalse(result, "Incorrect anagram should return False")

    def test_is_solved(self):
        # Simulate a solved condition
        self.anagram.correct_answer = "silent"
        self.assertTrue(self.anagram.is_solved("silent"), "Correct answer should mark the puzzle as solved")

if __name__ == '__main__':
    unittest.main()

