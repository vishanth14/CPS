#Run length encoding 
text = input("Enter a string: ")

encoded = ""
count = 1

for i in range(len(text)):
    if i < len(text) - 1 and text[i] == text[i+1]:
        count += 1
    else:
        encoded += text[i] + str(count)
        count = 1

print("Encoded string:", encoded)
