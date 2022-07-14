class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # recursion is used here to find all unique combinations of candidates whose sum equal to target
        
        def dfs(cur, path):
            if cur == 0:
                res.append(path)
            for n in candidates:
                if n > cur:  # cuz candidates is sorted list
                    break
                if path and n < path[-1]:  # Due to requirement of unique combinations, can't use previous number used already
                    continue
                
                dfs(cur - n, path + [n])
                
        res = []
        candidates.sort()
        dfs(target, [])
        return res
