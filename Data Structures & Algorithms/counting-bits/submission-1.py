class Solution:
    def countBits(self, n: int) -> List[int]:
        #this is a dynamic programming problem
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            #ans for i = ans for i // 2, plus 1 if i is odd
            dp[i] = dp[i >> 1] + ( i & 1)
        #return dp
        return dp