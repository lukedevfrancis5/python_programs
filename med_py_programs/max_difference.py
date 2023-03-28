from typing import List


def max_difference(nums: List[int]) -> int:
    max_diff = 0
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            diff = abs(nums[i] - nums[j])
            if diff > max_diff:
                max_diff = diff
        return max_diff        

'''
def max_difference(nums: List[int]) -> int:
    value = max(nums) - min(nums)
    return value   
'''                      
            
nums = 1, 2, 3, 4, 5

result = max_difference(nums)

print(result)