import random
class Force:
    units = 0
    def __init__(self, unit):
        self.units = unit
        print("units: ", self.units)

    # roll dice and see who wins
    def Attack(self, p2):
        dice1 = random.randint(1 ,6)
        dice2 = random.randint(1, 6)

        if (dice1 == dice2):
            return self.Attack(p2)

        # player 1 dice is higher
        if (dice1 > dice2):
            p2.units -= 1
            print("player 1 wins (p1: %s units left, p2: %s units left)" % (self.units, p2.units))

        # player 2 dice is higher
        if (dice2 > dice1):
            self.units -= 1
            print("player 2 wins (p1: %s units left, p2: %s units left)" % (self.units, p2.units))
