
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length_nums  = len(nums)
        low_pointer  = 0
        high_pointer = 1

        while high_pointer <= length_nums-1:
            if nums[low_pointer] == 0 and nums[high_pointer] != 0:

                nums[low_pointer], nums[high_pointer] = nums[high_pointer], nums[low_pointer]
                low_pointer                          += 1
                high_pointer                         += 1

            while high_pointer <= length_nums-1 and nums[high_pointer] == 0:
                high_pointer += 1


if __name__ == '__main__':
    solution = Solution()
    solution.moveZeroes([0,1,0,3,12])