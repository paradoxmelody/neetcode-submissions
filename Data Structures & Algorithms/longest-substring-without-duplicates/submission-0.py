class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #store : character -> its latest index
        last_seen = {}
        left = 0
        max_length = 0

        #right pointer expands the window
        for right in range(len(s)):
            char = s[right]

            #if char is alrealdy in window and it's last position is >= left
            if char in last_seen and last_seen[char] >= left:
                #move left pointer past the previous occurence
                left = last_seen[char] + 1
            #update last seen position of current char
            last_seen[char] = right

            #calculate current window size and update max
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        return max_length
        