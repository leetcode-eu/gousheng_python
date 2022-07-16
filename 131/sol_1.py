class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # backtracking method
        
        if not s:
            return []
        
        def IsPalindrome(partial_string):
            return partial_string == partial_string[::-1]
        
        def dfs(input_string, combination):
            
            if len(input_string) == 0:
                result.append(combination)
                return
            
            for sep_idx in range(len(input_string)):
                left = input_string[:sep_idx+1]
                right = input_string[sep_idx+1:]

                if IsPalindrome(left):
                    dfs(right, combination+[left])
            
        result = []
        dfs(s,[])
        
        return result
