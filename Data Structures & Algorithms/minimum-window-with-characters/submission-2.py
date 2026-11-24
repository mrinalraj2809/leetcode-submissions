class Solution:
           
    def minWindow(self, s: str, t: str) -> str:
        # If either or s or t is empty then result is empty
        if not s or not t:
            return ""
        
        required = {}
        # counted the t: A dict with characters as key and values as a freq, order is not preserved
        for c in t:
            required[c] = required.get(c, 0) + 1
        
        window = {}
        # initialising the dynamic sliding window 
        left = 0
        have = 0
        need = len(required) # need count of non-duplicated characters of the t string

        min_len = float("inf") # initilaising with max value possible
        min_start = 0

        for right in range(len(s)):
            # adding the current character in window
            c = s[right]
            window[c] = window.get(c, 0) + 1 # initialise the dict with its freq count
            # check if the character satisfies the requirement
            if c in required and window[c] == required[c]: # see if the freq of charcs encounters in substring matches with the t string freq dict, increase the counter of have; until it meets the needs (i.e. non ordered t string freq counter for each char)
                have += 1
            
            #shrink the window while its valid
            # shrink from left and stop until any char in s is present in t (i.e the window for that left char count is less than that char required (t string) count)
            while have == need:
                # update the smallest window
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    min_start = left
                # Remove the leftmost character
                left_char = s[left]
                window[left_char] -= 1

                if (
                    left_char in required
                    and window[left_char] < required[left_char]
                ):
                    have -= 1

                left += 1

        # if there was no such string of t present in s then min_len never gets initialised hence return empty string
        if min_len == float("inf"):
            return ""
        # if min_len is initialised then use the min_start and min_len indices from the original string to return the min window substring
        return s[min_start:min_start + min_len]