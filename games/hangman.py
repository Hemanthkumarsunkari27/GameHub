# gamehub/games/hangman.py

from games.base_game import BaseGame

class Hangman(BaseGame):
    def __init__(self, word):
        self.word = word
        self.guesses = []
        self.max_attempts = 6

    def display_word(self):
        display = ''.join([letter if letter in self.guesses else "_" for letter in self.word])
        print(f"Word: {display}")

    def play(self):
        attempts = 0
        while attempts < self.max_attempts:
            self.display_word()
            guess = input(f"Guess a letter (attempts left: {self.max_attempts - attempts}): ").lower()
            if guess in self.guesses:
                print("You already guessed that letter.")
            elif guess in self.word:
                self.guesses.append(guess)
                if all(letter in self.guesses for letter in self.word):
                    print(f"Congratulations! You guessed the word: {self.word}")
                    return
            else:
                attempts += 1
            if attempts == self.max_attempts:
                print(f"You lost! The word was: {self.word}")
