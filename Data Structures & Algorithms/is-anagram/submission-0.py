class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #this doesn't do much does it
        clean_s = s.replace(" ", "").lower()
        clean_t = t.replace(" ", "").lower()

        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)


 