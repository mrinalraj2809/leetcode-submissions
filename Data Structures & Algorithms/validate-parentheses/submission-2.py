class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 !=0:
            return False
        res = []
        res.append('-1')
        for b in s:
            if b in ['(', '{', '[']:
                res.append(b)
            else:
                v = res.pop()
                if v == '-1':
                    return False
                if b == ')' and v != '(':
                    return False
                elif b == '}' and v != '{':
                    return False
                elif b == ']' and v != '[':
                    return False
        return True if len(res) == 1 else False