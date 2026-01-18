import random

class GuessGame:
    def __init__(self):
        self.secret_number = random.randint(1, 10)

    def start(self):
        print ("24/14412...project...")
        print("Try to guess my number between 1 and 10")
        guess = int(input("Your guess: "))

        if guess == self.secret_number:
            print("Awesome! You got it right.")
        elif guess < self.secret_number:
            print("Too low, try again next time.")
        else:
            print("Too high, better luck next time.")

if __name__ == "__main__":
    game = GuessGame()
    game.start()
