class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #create a hashset
        hashSet = set(nums)
        #initialize maxmimum sequence length
        max_length = 0
        
        #process each number in the original array
        for current_num in nums:
            # ONLY start counting if this is the START of a sequence
            if current_num - 1 not in hashSet:
                sequence_end = current_num
                
                while sequence_end in hashSet:
                    #Remove processed numbers to avoid reprocessing
                    hashSet.remove(sequence_end)
                    sequence_end += 1
                #update the maximum length found so far
                max_length = max(max_length, sequence_end - current_num)
        
        return max_length