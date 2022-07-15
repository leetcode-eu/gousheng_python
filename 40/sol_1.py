class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(cur_diff, combination_set, starting_index):

            if cur_diff == 0:  # equal

                if combination_set not in result:
                    result.append(combination_set)

                return

            for idx in range(starting_index, len(candidates)):  # 相当于是做了树的剪枝
                 
                if idx > starting_index and candidates[idx] == candidates[idx-1]:  # 树的深度遍历会遍历到 repeated numbers 的情况, 就不需要在广度 level 上再添加树枝了，否则会报超时
                    continue
                
                num = candidates[idx]
                if num > cur_diff:
                    break  # sum would be > target

                dfs(cur_diff - num, combination_set + [num], idx+1)  # idx+1 is the difference from question 39 because of Each number in candidates 
                # may only be used once in the combination.

        candidates.sort()
        result = []
        dfs(target, [], 0)

        return result
