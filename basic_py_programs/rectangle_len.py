
prompt = input("What shape would you like to find the area for a rectangle?: ")

if prompt == "yes".lower():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    
    area = length * width
    print(f"The area of the rectangle is: {area}")
elif prompt == "no".lower():
    print("Thats fine. I'll see you later!")  