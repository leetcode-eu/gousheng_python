class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # recursion is used here to find all unique combinations of candidates whose sum equal to target ; 
        # For correct path, we return the dfs when sum = target, otherwise for incorrect path(s), we break it when sum is definitely > target
        
        def dfs(cur_diff, path):
            if cur_diff == 0:  # current_sum = target
                res.append(path)
                return
                
            for num in candidates:
                
                if path and num < path[-1]:  # Due to requirement of unique combinations, can't use previous number used already
                    continue
                
                if num > cur_diff:  # the sum would be > target cuz candidates is sorted list
                    break
                
                # current_sum < target, so we add n to the path
                dfs(cur_diff - num, path + [num])
                
        res = []
        candidates.sort()
        dfs(target, [])
        
        return res
