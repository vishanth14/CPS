# Integer Palindrome checker
num = int(input("Enter an integer: "))

original = num

rev = 0
while num > 0:
    digit = num % 10      
    rev = rev * 10 + digit  
    num = num // 10       

if original == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")