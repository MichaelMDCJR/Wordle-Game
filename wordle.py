import random


class Wordle:
    def __init__(self):
        self.current_winner = None
        self.words = ["robot"]
        self.rand_int = random.randrange(len(self.words))
        self.current_word = self.words[self.rand_int]
        self.history = []
        self.word_length = 5
        self.attempts = 6

    def guess(self, word):
        if self.attempts < 0:
            return "No attempts left!"

        self.attempts -= 1
        print(self.attempts)
        result = self.check_word(word)
        self.history.append((word, result))
        if self.attempts == 0:
            return "The word was: " + self.current_word
        if word == self.current_word:
            return "Correct, you guessed it!"
        return result

    def check_word(self, word):
        result = []
        for i in range(self.word_length):
            if word[i] == self.current_word[i]:
                result.append("correct")
            elif word[i] in self.current_word:
                result.append("present")
            else:
                result.append("absent")
        return result

    def get_attempts(self):
        return self.attempts
