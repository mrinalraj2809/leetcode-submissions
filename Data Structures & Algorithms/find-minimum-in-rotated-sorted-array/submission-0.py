class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        l = 0
        r = len(nums)-1
        mini = nums[r]
        while l<r:
            mid = ( l + r ) // 2
            if nums[mid] > mini:
                l = mid + 1
            else:
                mini = nums[mid]
                r = mid
        return mini

