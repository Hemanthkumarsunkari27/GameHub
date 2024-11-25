# gamehub/games/anagram.py

import random
from games.base_game import BaseGame

class Anagram(BaseGame):
    def __init__(self, words):
        self.words = words

    def play(self):
        word = random.choice(self.words)
        scrambled = ''.join(random.sample(word, len(word)))
        print(f"Unscramble this word: {scrambled}")
        guess = input("Your guess: ")
        if guess.lower() == word.lower():
            print("Correct!")
        else:
            print(f"Wrong! The correct word was {word}.")
