#Conditional operation on even and odd numbers
num = int(input("Enter a number: "))

if num % 2 == 0:
    result = num ** 2   
    print(f"{num} is even. Its square is {result}.")
else:
    result = num ** 3   
    print(f"{num} is odd. Its cube is {result}.")