n = int(input('Enter number: '))

Sum = 0
ctr = 0
for i in str(n):
    if ctr % 2 == 0:
        Sum += int(i)

    else:
        Sum -= int(i)
    ctr += 1

if Sum == 0:
    print('True')

else:
    print('False')