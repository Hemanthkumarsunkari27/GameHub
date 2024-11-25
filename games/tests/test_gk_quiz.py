# tests/test_gk_quiz.py

import unittest
from games.gk_quiz import GKQuiz

class TestGKQuiz(unittest.TestCase):
    
    def setUp(self):
        # Setup any pre-test configurations or initializations
        self.quiz = GKQuiz()

    def test_question_format(self):
        question = self.quiz.get_random_question()
        self.assertIsInstance(question, str, "The question should be a string")

    def test_correct_answer(self):
        question, correct_answer = self.quiz.get_question_and_answer()
        user_answer = correct_answer  # simulate correct answer
        self.assertTrue(self.quiz.check_answer(question, user_answer), "Answer should be correct")

    def test_incorrect_answer(self):
        question, correct_answer = self.quiz.get_question_and_answer()
        user_answer = "Wrong Answer"  # simulate incorrect answer
        self.assertFalse(self.quiz.check_answer(question, user_answer), "Answer should be incorrect")

if __name__ == '__main__':
    unittest.main()

