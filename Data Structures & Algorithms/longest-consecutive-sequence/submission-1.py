class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #create a hashset
        hashSet = set(nums)
        max_length = 0
        
        for current_num in nums:
            # ONLY start counting if this is the START of a sequence
            if current_num - 1 not in hashSet:
                sequence_end = current_num
                
                while sequence_end in hashSet:
                    hashSet.remove(sequence_end)
                    sequence_end += 1
                
                max_length = max(max_length, sequence_end - current_num)
        
        return max_length