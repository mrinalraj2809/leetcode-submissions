class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)-1):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                a = nums[i]
                b = nums[j]
                c = nums[k]
                if b + c < -a:
                    j += 1
                elif b + c > -a:
                    k -=1
                else:
                    res.add((a, b, c))
                    j += 1
        return list(res)
        # nums.sort()
        # res = set()
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.add((nums[i], nums[j], nums[k]))
        # return list(res)
        