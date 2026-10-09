class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set(nums)
        p = len(x)
        q = len(nums)
        if p != q:
            return True
        return False