class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # recursion is used here to find all unique combinations of candidates whose sum equal to target ; 
        # For correct path, we return the dfs when sum = target, otherwise for incorrect path(s), we break it when sum is definitely > target
        
        def dfs(cur_diff, path, starting_index):
            if cur_diff == 0:  # current_sum = target
                res.append(path)
                return
                
            for num in candidates[starting_index:]:
                
                if num > cur_diff:  # the sum would be > target cuz candidates is sorted list
                    break
                
                # current_sum < target, so we add num to the path
                dfs(cur_diff - num, path + [num], candidates.index(num))  # since same number may be chosen from candidates an unlimited number of times, 
                # the starting_index of candidates for next dfs could be the identical to the current index
        
        candidates.sort()
        res = []
        dfs(target, [], 0)
        
        return res
