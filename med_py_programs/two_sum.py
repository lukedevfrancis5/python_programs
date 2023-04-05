
# returns indices of the two numbers such that they add up to target.

target = 6
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i + 1:]):
            if num1 + num2 == target:
                return  ('[' + str(i) + ', ' + str(i+j+1) + ']')

nums = [3, 2, 4]
print(twoSum(nums, target))