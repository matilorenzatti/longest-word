import random
import string

class Game:
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for x in range(9)]


    def is_valid(self, word: str) -> bool:

        """Return True if and only if the word is valid, given the Game's grid"""

        if word is None:
            return False

        if not isinstance(word,str):
            return False

        if len(word) > 9:
            return False

        letters = self.grid.copy()

        for letter in word:
            if letter in letters:
                letters.remove(letter)

            else:
                return False

        return True
