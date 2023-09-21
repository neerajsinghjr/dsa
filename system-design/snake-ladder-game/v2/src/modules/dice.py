from random import randint


class Dice:

    def __init__(self, dice=1):
        self.dice = dice

    def roll(self):
        lower_bound = self.dice * 1
        upper_bound = self.dice * 6
        return  randint(upper_bound, lower_bound)