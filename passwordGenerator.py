import random
lower = "qwertyuiopasdfghjklzxcvbnm"
upper = lower.upper()
numbers = "1234567890"
symbols = "!@#$%^&*?[]{}+_:;"

combination_1 = lower + upper + numbers + symbols
combination_2 = lower + upper + symbols + numbers
combination_3 = upper + lower + numbers + symbols
combination_4 = upper + lower + symbols + numbers 
combination_5 = numbers + lower + upper + symbols
combination_6 = numbers + lower + symbols + upper
combination_7 = numbers + upper + lower + symbols
combination_8 = numbers + upper + symbols + lower
combination_9 = numbers + symbols + upper + lower
combination_10 = numbers + symbols + lower + upper

def createPasswords(length):
    password_set_1 = "".join(random.sample(combination_1,length))
    password_set_2 = "".join(random.sample(combination_2,length))
    password_set_3 = "".join(random.sample(combination_3,length))
    password_set_4 = "".join(random.sample(combination_4,length))
    password_set_5 = "".join(random.sample(combination_5,length))
    password_set_6 = "".join(random.sample(combination_6,length))
    password_set_7 = "".join(random.sample(combination_7,length))
    password_set_8 = "".join(random.sample(combination_8,length))
    password_set_9 = "".join(random.sample(combination_9,length))
    password_set_10 = "".join(random.sample(combination_10,length))
    print("--- Choose password you want ---")
    print("Password set 1:",password_set_1)
    print("Password set 2:",password_set_2)
    print("Password set 3:",password_set_3)
    print("Password set 4:",password_set_4)
    print("Password set 5:",password_set_5)
    print("Password set 6:",password_set_6)
    print("Password set 7:",password_set_7)
    print("Password set 8:",password_set_8)
    print("Password set 9:",password_set_9)
    print("Password set 10:",password_set_10)
    print("\nGenerate passwords success...!")
    print("----------------------------------")

def generatePassword():
    while(True):
        try:
            length = int(input("Enter length of password: "))
            if length >= 8 :
                createPasswords(length)
                return
            else:
                print("Required: Length at least 8")
        except ValueError:
            print("Failed: Length is must be an integer.")
            continue

generatePassword()