class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Stack to store indices n descending order
        stack = []
        n = len(temperatures)
        # Initialize result array  
        result = [0] * n
      
        # Traverse temperatures from right to left
        for i in range(n - 1, -1, -1):
            # Pop elements from stack  
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
          
            # If stack is not empty, top element is the next warmer day
            if stack:
                result[i] = stack[-1] - i
          
            # Add current index to stack for future comparisons
            stack.append(i)
      
        return result
