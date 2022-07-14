class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        dic = {'2':"abc", '3':"def", '4':"ghi", '5':"kjl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        length_of_number = len(digits)
        result = [item for item in dic[digits[0]] ]
        for i in range(1, length_of_number):
            result = [item+alphabet  for item in result for alphabet in dic[digits[i]] ]
        
        return result
