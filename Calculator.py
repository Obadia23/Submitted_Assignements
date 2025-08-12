# Simple Calculator

# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user for an operation
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation based on the user's selection
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        exit()
else:
    print("Invalid operation entered.")
    exit()

# Display the result
print(f"{num1} {operation} {num2} = {result}")

print("thank you for trying...")
