
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        # sort the nums array
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                i += 1
                k -= 1
            else:
                break
        
        # resort modified nums       
        nums.sort()
        
        # if remaining k > 0, meaning number in current nums are all positive
        #     if k is even: flip nums[0] for k times, equivalent to no operation
        #     if k is even: flip nums[0] for k times, equivalent 1 flip
        if k%2 != 0:
            nums[0] = -nums[0]
            
        return sum(nums)
