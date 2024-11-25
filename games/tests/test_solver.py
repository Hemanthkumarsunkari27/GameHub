# tests/test_solver.py

import unittest
from games.solver import Solver

class TestSolver(unittest.TestCase):

    def setUp(self):
        self.solver = Solver()

    def test_solve_math_problem(self):
        # Test solving a math problem
        problem = "2 + 3"
        solution = self.solver.solve_math_problem(problem)
        self.assertEqual(solution, 5, "Solver should correctly solve simple math problems")

    def test_solve_word_problem(self):
        # Test solving a simple word problem
        problem = "What is the synonym of happy?"
        solution = self.solver.solve_word_problem(problem)
        self.assertIn("joyful", solution, "Solver should include 'joyful' in synonyms for 'happy'")

    def test_is_solved_correct(self):
        # Simulate a solved condition
        result = self.solver.is_solved(True)
        self.assertTrue(result, "Solver should mark the problem as solved if correct")

    def test_is_solved_incorrect(self):
        # Simulate an unsolved condition
        result = self.solver.is_solved(False)
        self.assertFalse(result, "Solver should not mark the problem as solved if incorrect")

if __name__ == '__main__':
    unittest.main()
