#FizzBuzz
num=int(input("Enter the Number:"))
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0 and num%5!=0:
    print("Fizz")
elif num%3!=0 and num%5==0:
    print("Buzz")
else:
    print("The entered number is not divisible by 3 and 5")
