import random

class Card:
    suits = ["diamonds", "hearts", "spades", "clubs"]
    numbers = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]  
    def __int__(self):
        suit = None
        value = None
        color = None
        imagePath = None
    def randomCard(self):
        self.suit = random.choice(self.suits)
        self.value = random.choice(self.numbers)
    def getPath(self):
        self.imagePath = "playing cards\\" + str(self.value) + "_of_" + self.suit + ".png"

# "playing cards\\" + str(number) + "_of_" + suit + ".png"