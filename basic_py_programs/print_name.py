# takes in user input and gives a response 

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
age = int(input("What is your age?: "))

if age <= 20:
    response = "It's great that you are this young to be learning to code.!" 
elif age >21:
    response = "You are on the older side of programing but good thing is, it's for all ages!"  

print(f"Hello, {first_name} {last_name}! You are {age} years old. {response}")