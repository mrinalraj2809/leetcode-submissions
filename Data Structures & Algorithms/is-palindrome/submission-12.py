class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        strs = ""
        for i in range(len(s)):
            if s[i].isalnum():
                strs += s[i]
        rev = strs[::-1]
        return strs.lower() == rev.lower()
            
