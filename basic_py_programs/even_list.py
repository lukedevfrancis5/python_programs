# takes in user input and prints even numbers 

input_str = input("Enter a list a numbers: ")
nums = [int(num) for num in input_str.split()]
new_list = []

for num in nums:
    if num % 2 == 0:
        new_list.append(num)

print(f"The even numbers are: {new_list}")