green_text = "\033[32m"
yellow_text = "\033[33m"
pink_text = "\033[35m"
reset_color = "\033[0m"
randomEmail = "qwertyuiopasdfghjklzxcvbnm0123456789"

def createTesterWithGmail(n): 
    members = [member for member in range(1, n+1)]
    for i in range(1,len(members)+1):
        email = f"> {green_text}tester0{i}@gmail.com{reset_color}"
        print(email)

def createTesterWithHotmail(n): 
    members = [member for member in range(1, n+1)]
    for i in range(1,len(members)+1):
        email = f"> {yellow_text}tester0{i}@hotmail.com{reset_color}"
        print(email)

def createTesterWithOrganize(n,organize): 
    members = [member for member in range(1, n+1)]
    for i in range(1,len(members)+1):
        email = f"> {pink_text}tester0{i}@{organize}{reset_color}"
        print(email)

def createEmail():
    print("--- Choose ---")
    print("Gmail(1) Hotmail(2) Organize(3)\n")
    get = int(input("Choice : "))
    if (get == 1):
        print("--- Gmail ---")
        n = int(input(f"size: "))
        createTesterWithGmail(n)
    elif (get == 2):
        print("--- Hotmail ---")
        n = int(input("size: "))
        createTesterWithHotmail(n)
    elif (get == 3):
        print("--- Organize ---")
        n = int(input("size: "))
        name = input("@ : ")
        createTesterWithOrganize(n,name)
    else:
        print("Choose again ...")

createEmail()