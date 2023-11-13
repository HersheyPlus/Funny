import random

true = True

def targetNumber():
    while(True):
        try:
            start = int(input("Enter number start: "))
            end = int(input("Enter number end: "))
            break
        except ValueError:
            print("Please enter only number ")
            continue
    targetNumber = random.randint(start, end)
    return targetNumber

def guessNumberSetRound():
    while True:
        try:
            round = int(input("Enter chance you: "))
            while round > 0:
                print(f"You chance(s) ({round}) left")
                try:
                    guess = int(input("Guess: "))
                except ValueError:
                    print("--- Enter only number ---")
                    continue
                if guess == targetNumber():
                    print("----- Congraturation -----")
                    return
                elif guess > targetNumber():
                    print(">> Too high <<")
                else:
                    print(">> Too low <<")
                round -= 1
                if round == 0:
                    print("\n----- Out of chances. The correct number was", targetNumber(), "-----")
                    return
        except ValueError:
            print("--- Enter only number ---")
            continue


def guessNumberDefault():
    round = 5
    while round > 0:
        print(f"You have {round} chance(s) left")
        try:
            guess = int(input("Guess: "))
        except ValueError:
            print("--- Enter only numbers ---")
            continue
        if guess == targetNumber():
            print("----- Congratulations! You guessed correctly! -----")
            break  # Exit the loop when guess is correct
        elif guess > targetNumber():
            print(">> Too high <<")
        else:
            print(">> Too low <<")
        round -= 1
    if round == 0:
        print("----- \nOut of chances. The correct number was", targetNumber(), "-----")


def guessNumber():
    targetNumber()
    while true:
        is_setRound = input("Do you need to set chance ? (y/n): ")
        try:
            if is_setRound == "y":
                guessNumberSetRound()
                true = False
            elif is_setRound == "n":
                guessNumberDefault()
                true = False
            else:
                print("--- Enter only y or n ---")
                continue
        except ValueError:
            print("--- Enter only y or n ---")
            continue

guessNumber()
