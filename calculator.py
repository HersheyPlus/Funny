print("Select operation you need")
print("1.Plus (+)\n2.Subtract (-)\n3.Times (x)\n4.Divide (÷)")
print("------------------------------------------------")

while (True):
    operation = int(input("Choose your operation (1/2/3/4): "))
    if (operation == 1 or operation == 2 or operation == 3 or operation == 4):
        try:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input, enter again...")
            continue
        if (operation == 1):
            print(f"{number_1} + {number_2} = {number_1+number_2}")
        elif (operation == 2):
            print(f"{number_1} - {number_2} = {number_1-number_2}")
        elif (operation == 3):
            print(f"{number_1} x {number_2} = {number_1*number_2}")
        else:
            print(f"{number_1} ÷ {number_2} = {number_1/number_2}")
            
        next_to_operation = input("Do you need to calculate next (y/n): ")
        if next_to_operation == 'n':
            break
    else:
        print("Choose between 1-4 operation")