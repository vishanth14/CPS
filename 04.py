#Simple calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"
quotient = num1 // num2 if num2 != 0 else "Undefined (division by zero)"
remainder = num1 % num2 if num2 != 0 else "Undefined (division by zero)"

print("\nResults:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")