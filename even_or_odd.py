# takes in num and outputs whether or not num is even or odd

prompt = int(input("Enter a number to see if it's even or odd: "))

if prompt % 2 == 0:
    print("The number you entered is even.")
else:
    print("The number you entered is odd.")