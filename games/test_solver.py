# gamehub/games/solver.py

from games.base_game import BaseGame

class Solver(BaseGame):
    def __init__(self, equation):
        self.equation = equation

    def play(self):
        try:
            solution = eval(self.equation)
            print(f"The solution to {self.equation} is: {solution}")
        except Exception as e:
            print(f"Error solving equation: {e}")
