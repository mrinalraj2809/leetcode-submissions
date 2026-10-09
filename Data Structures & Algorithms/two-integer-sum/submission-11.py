class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, n in enumerate(nums):
            if target - n in nums and nums.index(target - n) != i:
                return [nums.index(n), nums.index(target-n, nums.index(n)+1)]