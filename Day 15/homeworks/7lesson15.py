operation = input("choose between +,-,*,/,:")
number1 = int(input("Enter first:"))
number2 = int(input("Enter second:"))

if operation == "+":
    print(number1 + number2)

elif operation == "-":
    print(number1 - number2)

elif operation == "*":
    print(number1 * number2)

elif operation == "/":
    print(number1 / number2)

else:
    print("invalid operation")