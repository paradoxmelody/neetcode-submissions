class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
      
        # dp[i] represents the number of ways to decode s[0:i]
        # dp[0] = 1 represents empty string (base case)
        dp = [1] + [0] * n
      
        # Iterate through each character in the string
        for i in range(1, n + 1):
            # Single digit decoding: check if current character is valid (1-9)
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
          
            # Two digit decoding: check if previous two characters form valid number (10-26)
            if i >= 2 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
      
        # Return the number of ways to decode the entire string
        return dp[n]
        