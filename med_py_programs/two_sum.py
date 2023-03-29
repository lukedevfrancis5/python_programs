
# return indices of the two numbers such that they add up to target.

target = 9
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:]):
                if num1 + num2 == target:
                    print('[' + str(i) + ', ' + str(i+j+1) + ']')

nums = [2, 7, 11, 15]
twoSum(nums, target)