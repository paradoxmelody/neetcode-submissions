
class Solution {
    public String minWindow(String s, String t) {
        // Frequency map for characters needed from string t
        int[] targetFreq = new int[128];
        // Frequency map for characters in current window
        int[] windowFreq = new int[128];
      
        // Count frequency of each character in t
        for (char ch : t.toCharArray()) {
            targetFreq[ch]++;
        }
      
        int sourceLen = s.length();
        int targetLen = t.length();
      
        // Variables to track the minimum window
        int minWindowStart = -1;   
        int minWindowLen = sourceLen + 1;   
        int validCharCount = 0;   
      
        // Sliding window approach with two pointers
        int left = 0;
        for (int right = 0; right < sourceLen; right++) {
            // Expand window by including character at right pointer
            char rightChar = s.charAt(right);
            windowFreq[rightChar]++;
          
            // If this character contributes to a valid match, increment count
            if (windowFreq[rightChar] <= targetFreq[rightChar]) {
                validCharCount++;
            }
          
            // Contract window from left while it remains valid
            while (validCharCount == targetLen) {
                // Update minimum window if current window is smaller
                if (right - left + 1 < minWindowLen) {
                    minWindowLen = right - left + 1;
                    minWindowStart = left;
                }
              
                // Remove leftmost character from window
                char leftChar = s.charAt(left);
              
                // If removing this character breaks validity, decrement count
                if (windowFreq[leftChar] <= targetFreq[leftChar]) {
                    validCharCount--;
                }
              
                windowFreq[leftChar]--;
                left++;
            }
        }
      
        // Return empty string if no valid window found, otherwise return minimum window
        return minWindowStart < 0 ? "" : s.substring(minWindowStart, minWindowStart + minWindowLen);
    }
}
