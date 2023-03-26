# takes in user input and adds the even numbers 

user_input = input("Enter a list of numbers: ")

nums = [int(num) for num in user_input.split()]

added_even_nums = 0 

for num in nums:
    if num % 2 == 0:
        added_even_nums += num
    

print(f"{added_even_nums}")
        
    

