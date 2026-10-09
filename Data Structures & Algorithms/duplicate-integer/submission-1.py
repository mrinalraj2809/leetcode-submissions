class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        res = defaultdict(int) # default value 0
        for v in nums:
            # print("value", v)
            # print("res", res)
            if res[v] == 0:
                res[v] = 1
            else:
                return True
        return False
        