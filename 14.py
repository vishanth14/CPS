#Vowels and consonants counter
text = input("Enter a string: ")

vowels = 0
consonants = 0

vowel_list = "aeiouAEIOU"

for ch in text:
    if ch.isalpha(): 
        if ch in vowel_list:
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)