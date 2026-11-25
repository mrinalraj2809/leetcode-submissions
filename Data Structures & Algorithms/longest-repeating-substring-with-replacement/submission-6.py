class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        # I need a dynamic sliding window where left and right increase based on two condition
        # 1. how many different characters it can endure
        # 2. how to shrink the window

        # left = 0
        # max_repeat = - float('inf')

        # need = 0
        # have = 
        # for right in range(len(s)):

        left = 0
        max_freq = 0
        max_length = 0

        freq = {}

        for right in range(len(s)):

            # Add the current character to the window
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Track the highest frequency of a character
            max_freq = max(max_freq, freq[s[right]])

            # If replacements exceed k, shrink the window
            while (right - left + 1) - max_freq > k:

                freq[s[left]] -= 1
                left += 1

            # Update the longest valid window
            max_length = max(max_length, right - left + 1)

        return max_length
                


        
        