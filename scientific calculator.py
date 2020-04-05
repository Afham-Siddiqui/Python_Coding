print("scientific calculator")
a = str(input("Do you want to start(yes/no)"))
if a == "yes":
    print("okay, You can use this calculator")

    operators = str(input("+ , - , / , * , math.sqrt , power , sin , cos , tan "))

    if operators == "+":
        number_1 = int(input("enter your number..."))
        number_2 = int(input("enter your number..."))
        print("The sum of", number_1, number_2, "is", (number_1 + number_2))

    if operators == "-":
        number_1 = int(input("enter your number..."))
        number_2 = int(input("enter your number..."))
        print("The subtraction of", number_1, number_2, "is", (number_1 - number_2))

    if operators == "/":
        number_1 = int(input("enter your number..."))
        number_2 = int(input("enter your number..."))
        print("The answer", number_1, number_2, "is", (number_1 / number_2))

    if operators == "*":
        number_1 = int(input("enter your number..."))
        number_2 = int(input("enter your number..."))
        print("The answer of", number_1, number_2, "is", (number_1 * number_2))

    import math
    if operators == "math.sqrt":
        number_1 = int(input("enter your number..."))
        print("The answer of", number_1, "is", math.sqrt(number_1))

    if operators == "power":
        number_1 = int(input("enter your number..."))
        number_2 = int(input("enter your number..."))
        print("The answer of", number_1, number_2, "is",  (number_1 ** number_2))
    if operators == "sin":
        number_1 = int(input("enter any angle..."))
        print("The answer of", number_1, "is", math.sin(number_1))

    if operators == "cos":
        number_1 = int(input("enter any angle..."))
        print("The cos of ", number_1, "is", math.cos(number_1))

    if operators == "tan":
        number_1 = int(input("enter any angle..."))
        print("The tan of", number_1, "is", math.tan(number_1))

else:
    print("good bye")
