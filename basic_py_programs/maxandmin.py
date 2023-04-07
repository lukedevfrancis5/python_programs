from typing import List, Tuple

def max_and_min(nums:List[int]) -> Tuple[int, int]:
    max_num = max(nums)
    min_num = min(nums)
    return max_num, min_num


print(max_and_min([1,2,3,4,5,6]))