class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #start with two pointers on both ends
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            #calculate current area
            width = right - left
            current_height = min(heights[right], heights[left])
            current_area = width * current_height

            #now calc the max wata
            max_water = max(max_water, current_area)

            #if left is shorter move to the right else if right is shorter move to the left
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_water
        