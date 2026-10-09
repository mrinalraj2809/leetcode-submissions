class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        from collections import defaultdict
        res_s = defaultdict(int)
        res_t = defaultdict(int)
        for c in s:
            res_s[c] += 1
        for c in t:
            res_t[c] += 1
        for k, v in res_s.items():
            if res_s[k] != res_t[k]:
                return False
        return True


        