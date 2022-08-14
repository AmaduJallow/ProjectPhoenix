import random


class Guesser:
    random = 0

    def guesser(self):
        ranger = int(input("Please enter your upper bound: "))
        randomValue = random.randint(1, ranger + 1)

        while True:
            self.random = int(input(f"Please enter your guess between 1 t0 {ranger}: "))

            if self.random == randomValue:
                print("You win")
                break
            else:
                print("Please try again")
                continue


TOFM = Guesser()
TOFM.guesser()
