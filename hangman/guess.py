class Guess():
    def __init__(self, value):
        self.value = value

    def isvalid(self):
        return len(self.value) == 1 and self.value.isalpha()

    def isguessed(self, guesses):
        return self.value in guesses

    def iscorrect(self, word):
        return self.value in word

    def getvalue(self):
        return self.value
