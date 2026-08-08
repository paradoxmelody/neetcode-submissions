from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        #Iterate through each number as the first element
        for i in range(n - 1):
            # Calculate the difference needed to reach the target
            diff = target - numbers[i]

            # Binary search template to find first index where numbers[mid] >= difference
            left, right = i + 1, n - 1
            first_true_index = -1

            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] >= diff:
                    first_true_index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            # Check if the complement exists at the found position
            if first_true_index != -1 and numbers[first_true_index] == diff:
                # Return 1-indexed positions
                return [i + 1, first_true_index + 1]

        return []  # Problem guarantees a solution exists
 