class Solution {
    public int characterReplacement(String s, int k) {
        // Array to store frequency count of each uppercase letter (A-Z)
        int[] charFrequency = new int[26];
      
        // Left pointer of the sliding window
        int left = 0;
      
        // Maximum frequency of any single character in the current window
        int maxFrequency = 0;
      
        // Length of the input string
        int length = s.length();
      
        // Iterate through the string with right pointer
        for (int right = 0; right < length; right++) {
            // Increment frequency of current character and update max frequency
            int currentCharIndex = s.charAt(right) - 'A';
            charFrequency[currentCharIndex]++;
            maxFrequency = Math.max(maxFrequency, charFrequency[currentCharIndex]);
          
            // Check if current window is valid
            int windowSize = right - left + 1;
            int charactersToReplace = windowSize - maxFrequency;
          
            if (charactersToReplace > k) {
                // Shrink window from left by moving left pointer
                // Decrement frequency of the character being removed from window
                int leftCharIndex = s.charAt(left) - 'A';
                charFrequency[leftCharIndex]--;
                left++;
            }
        }
      
        // The final window size is the maximum valid substring length
        
        return length - left;
    }
}
