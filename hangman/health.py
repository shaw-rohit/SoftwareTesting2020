class Health:
    def __init__(self):
        self.health = 9

    def sethealth(self, damage=1):
        self.health -= damage

    def gethealth(self):
        return self.health
