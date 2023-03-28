# takes a list of integers as input and returns the two numbers that add up to zero

'''
Write a Python function that takes a list of integers as input and returns the two numbers 
that add up to zero. If there are no such numbers, the function should return None.
For example, if the input list is [1, 2, -3, 4, -2], the function should return (-2, 2), 
since -2 + 2 = 0. If the input list is [1, 2, 3], the function should return None, 
since there are no two numbers in the list that add up to zero.
'''

'''user_input = input("Enter some numbers: ")

num_list = [(int(num) for num in user_input.split())]

found_pair = False 

for i, num1 in enumerate(num_list):
    for j, num2 in enumerate(num_list[i + 1:]):
        if num1 + num2 == 0:
            found_pair = True
            print(f"({num1, num2})")
if not found_pair:
    print(f"None")
''' 

def find_pair(list):
    for i, num1 in enumerate(list):
        for j, num2 in enumerate(list[i+1:]):
            if num1 + num2 == 0:
                return (num1, num2)
    return None


list = [1, 2, -3, 4, -2]

result = find_pair(list)

print(result)
