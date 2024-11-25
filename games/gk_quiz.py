# gamehub/games/gk_quiz.py

from games.base_game import BaseGame

class GKQuiz(BaseGame):
    def __init__(self, questions):
        self.questions = questions

    def play(self):
        score = 0
        for question, answer in self.questions.items():
            user_answer = input(f"{question}: ")
            if user_answer.lower() == answer.lower():
                score += 1
        print(f"You scored {score}/{len(self.questions)}")
