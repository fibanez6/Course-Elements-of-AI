import random

def main():
    r = random.random()

    favourite = "bats"  # change this
    if r < 0.8:
        favourite = "dogs"
    elif r < 0.9:
        favourite = "cats"

    print("I love " + favourite) 


main()
