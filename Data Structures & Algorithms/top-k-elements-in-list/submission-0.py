from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        counts = list(freq.values())

        result = []

        for tuple_item in freq.most_common(k):
           result.append(tuple_item[0])  
        return result

       

        