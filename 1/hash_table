class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map will save the element: indice pair, as an element is saved in the hash_map,
        # it is waiting for the incoming complementary element (their sum = certain val) to pair up
        hash_map = {}
        
        for i in range(len(nums)):
            if target-nums[i] not in hash_map:
                hash_map[nums[i]] = i
            else:
                return hash_map[target-nums[i]], i
