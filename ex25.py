import random

def guess_number():
    print("Think of a number between 0 and 100.")
    min_num = 0
    max_num = 100
    guess = None
    trys = 0
#main game
    while guess != "c":
        trys += 1
        guess = random.randint(min_num, max_num)
        print(f"Is your number {guess}?")
        response = input("Enter 'h' if it's too high, 'l' if it's too low, or 'c' if it's correct: ")

        if response == "h":
            max_num = guess - 1
        elif response == "l":
            min_num = guess + 1
        elif response == "c":
            print("I guessed it! Your number is", guess)
            break
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")
    print(trys)
guess_number()

