class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        length = len(nums3)
        if length % 2 != 0:
            mid = length//2
            return nums3[mid]
        else:
            mid = length//2
            return (nums3[mid-1] + nums3[mid] ) / 2