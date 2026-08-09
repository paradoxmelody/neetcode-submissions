class Solution:
    def trap(self, height: List[int]) -> int:
        #two pointers
        n = len(height)
      
        #Store maximum height to the left and right of each position
        max_left = [0] * n
        max_right = [0] * n
      
        # Base cases: first elementfor right and last for left
        max_left[0] = height[0]
        max_right[n - 1] = height[n - 1]
      
        #Store the maximum height seen so far from the left
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])
      
        #Store the maximum height seen so far from the right
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])
      
        # Calculate trapped water at each position
        total_water = 0
        for i in range(n):
            water_level = min(max_left[i], max_right[i])
            total_water += water_level - height[i]
      
        return total_water