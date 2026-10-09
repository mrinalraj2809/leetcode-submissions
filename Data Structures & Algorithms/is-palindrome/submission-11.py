class Solution:
    def isPalindrome(self, s: str) -> bool:
        # res = s.replace(' ', '')
        # res = res.replace('?', '')
        # res = res.replace("'", '')
        # res = res.replace(',', '')
        # res = res.replace('?', '')
        res = s
        for c in res:
            if not c.isalpha() and not c.isnumeric():
                res = res.replace(c, '')
        res = res.lower()
        print(res)
        if len(res) <=1:
            return True 
        for i, c in enumerate(res):
            print(i, c)
            # if i <= len(s)/2 and s[i] != s[-(i+1)]:
            if res[i] != res[-(i+1)]:
                return False
            if i >= len(res)/2:
                return True
        