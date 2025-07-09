num1 = float(input("Enter first number: "))
operator = (input('Enter a valid operator(+ - * / or **): '))
num2 = float(input("Enter second number: "))
if operator == '+':
    result = num1 + num2
    print("Result: " + str(result))
elif operator == '-':
    result = num1 - num2
    print("Result: " + str(result))
elif operator == '*':
    result = num1 * num2
    print("Result: " + str(result))
elif operator == '-':
    result = num1 * num2
    print("Result: " + str(result))
elif operator == "**":
    result = num1 ** num2
    print("Result: " + str(result))
else:
    print({operator} + "is not a valid oparator.")
