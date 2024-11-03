number1 = input("Number1:")
operation = input("Operation (+, -, *, /): ")
number2 = input("Number2:")

if (operation == "+"):
    answer = int(number1) + int(number2)

if (operation == "-"):
    answer = int(number1) - int(number2)

if (operation == "*"):
    answer = int(number1) * int(number2)

if (operation == "/"):
    answer = int(number1) / int(number2)

print(answer)
