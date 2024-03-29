class Solution:
    def fib(self, n: int) -> int:
        # base case: dp[0] = 0, dp[1] = 1
        # pattern: F(n) = F(n - 1) + F(n - 2), for n > 1.
        
        if n==0 or n==1:
            return n
        
        # when n=3, there are 4 numbers in Fibonacci sequence in total, 
        # when n=4, there are 5 numbers in Fibonacci sequence in total,
        # it should be "n+1" in range()
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n]
        
        
