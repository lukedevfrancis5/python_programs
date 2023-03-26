# takes in list of numbers and prints out the sum 

nums = input("Enter a list of numbers, seperated by commas: ")

num_list = nums.split(",")

total = 0

for num_str in num_list:
    num = int(num_str)

    total += num 

print(f"The sum of all the numbers is {total}")