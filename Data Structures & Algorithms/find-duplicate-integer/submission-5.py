class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return nums[i]
        
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
        # if len(nums) == 2:
        #     return nums[0]
        # slow = 0 
        # fast = 1
        # length = len(nums)
        # while True:
        #     if nums[slow] == nums[fast]:
        #         return nums[slow]
        #     slow += 1
        #     fast = (fast + 2)  % (length)
