from typing import List

# takes in list and outputs the unique numbers in list

def unique_list(nums:List[int]) -> List[int]:
    new_list = []
    for i, num in enumerate(nums):
        if nums.count(num) == 1:
            new_list.append(num)
    return new_list

print(unique_list([1,2,3,2,4])) 