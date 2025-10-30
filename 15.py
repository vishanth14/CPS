#String Palindrome checker
text = input("Enter a string: ")

text = text.lower()

if text == text[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")