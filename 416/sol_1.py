class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total_value = sum(nums)
        n = len(nums)
        
        # Only if total_value is even, nums can be partitioned into two subsets such that the sum of elements in both subsets is equal
        if total_value % 2 == 1:  
            return False
        
        target_value = total_value//2
            
        # Create the dynamic programming matrix
        dp_matrix = [[False]*(target_value+1) for _ in range(n+1)]
        dp_matrix[0][0] = True  # The reason why dp_matrix[0][0] is True is: it is the base case for succeeding cases in dp_matrix, e.g. nums[0] = 5, and when j is traversed to be 5, dp_matrix[0][5] becomes True
        
        for i in range(1, n+1):
            for j in range(target_value+1):
                if nums[i-1] > j:  # as nums[i] is already > j, just take a look at the previous one, i.e. dp_matrix[i-1][j]
                    dp_matrix[i][j] = dp_matrix[i-1][j]
                else:
                    dp_matrix[i][j] = dp_matrix[i-1][j] | dp_matrix[i-1][j-nums[i-1]]  # need to check both of previous one and wether difference between j and nums[i-1] is True
        
        return dp_matrix[-1][-1]
