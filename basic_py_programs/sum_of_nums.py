# gets a list of numbers and sums up even numbers

nums = input("Enter a list of numbers, seperated by commas: ")

nums_list = nums.split(",")

even_sum_total = 0

for num in nums_list:
    new_num = int(num)
    if new_num % 2 == 0:
        even_sum_total += new_num

print(f"The sum of even numbers is {even_sum_total}")


