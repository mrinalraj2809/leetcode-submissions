from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ob = Counter(list(s))
        sitems = ob.items()
        ob = Counter(list(t))
        titems = ob.items()
        print(sitems)
        print(titems)

        for k, v in sitems:
            if (k,v) not in titems:
                return False
        return True
        