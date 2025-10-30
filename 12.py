#Digit to text

num = input("Enter a number: ")

print("In words:")
for ch in num:
    if ch == '0':
        print("Zero", end=" ")
    elif ch == '1':
        print("One", end=" ")
    elif ch == '2':
        print("Two", end=" ")
    elif ch == '3':
        print("Three", end=" ")
    elif ch == '4':
        print("Four", end=" ")
    elif ch == '5':
        print("Five", end=" ")
    elif ch == '6':
        print("Six", end=" ")
    elif ch == '7':
        print("Seven", end=" ")
    elif ch == '8':
        print("Eight", end=" ")
    elif ch == '9':
        print("Nine", end=" ")
    else:
        print("Invalid", end=" ")
