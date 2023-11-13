import random
set = ["r","p","s"]
bot_random = random.sample(set,1)


while True:
    try:
        choice = input("Guess (r (rock) / s (scisser) / p (paper): ")
        if choice == "r" or choice == "s" or choice == "p":
            if bot_random == "r":
                if choice == "p":
                    print("You choose paper (p) and bot choose rock (r)")
                    print("paper (you) vs rock")
                    print("You win")
                    break
                elif choice == "s":
                    print("You choose scisser (s) and bot choose rock (r)")
                    print("scisser (you) vs rock")
                    print("You lose")
                    break
                else:
                    print("You choose rock (r) and bot choose rock (r)")
                    print("rock (you) vs rock")
                    print("You draw")
                    break

            elif bot_random =="p":
                if choice == "s":
                    print("You choose scisser (s) and bot choose paper (p)")
                    print("scisser (you) vs paper")
                    print("You win")
                    break
                elif choice == "r":
                    print("You choose rock (r) and bot choose paper (p)")
                    print("rock (you) vs paper")
                    print("You win")
                    break
                else:
                    print("You choose paper (p) and bot choose paper (p)")
                    print("paper (you) vs paper")
                    print("You draw")
                    break
                
            else:
                if choice == "r":
                    print("You choose rock (r) and bot choose scisser (s)")
                    print("rock (you) vs scisser")
                    print("You win")
                    break
                elif choice == "p":
                    print("You choose paper (p) and bot choose scisser (s)")
                    print("paper (you) vs scisser")
                    print("You lose")
                    break
                else:
                    print("You choose scisser (s) and bot choose scisser (s)")
                    print("scisser (you) vs scisser")
                    print("You draw")
                    break
        else:
            print("Error, Try again...")
            
    except ValueError:
        print("Choose between r / s /p")
        continue