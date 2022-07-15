class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        numbers = [1,2,3,4,5,6,7,8,9]
        
        def dfs(num_numbers_to_be_used, cur_diff, combination, starting_index):
            # compared to question 39 & 40, the number of numbers in a combination is fixed, it means the width of tree is fixed
            if num_numbers_to_be_used == 0:
                if cur_diff == 0:
                    result.append(combination)
                
                return
            
            for idx in range(starting_index, len(numbers)):
                num = numbers[idx]
                
                if num > cur_diff:
                    break
                
                dfs(num_numbers_to_be_used-1, cur_diff-num, combination+[num], idx+1)
            
        result = []
        dfs(k, n, [], 0)
        
        return result
