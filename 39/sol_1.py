class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # recursion is used here to find all unique combinations of candidates whose sum equal to target
        
        def dfs(cur_diff, path):
            if cur_diff == 0:  # current_sum = target
                res.append(path)
                
            for n in candidates:
                if n > cur_diff:  # the sum would be > target cuz candidates is sorted list
                    break
                
                if path and n < path[-1]:  # Due to requirement of unique combinations, can't use previous number used already
                    continue
                
                # current_sum < target, so we add n to the path
                dfs(cur_diff - n, path + [n])
                
        res = []
        candidates.sort()
        dfs(target, [])
        
        return res
