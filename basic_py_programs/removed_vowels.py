# takes in a string phrase and out puts phrase without vovewls 

string = input("Enter a phrase: ")

vowels = "aeiouAEIOU"

new_string = ""

for letter in string:
    if letter not in vowels:
        new_string += letter


print(f"The new string is {new_string}") 