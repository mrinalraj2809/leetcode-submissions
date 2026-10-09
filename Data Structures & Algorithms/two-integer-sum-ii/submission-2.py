class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1] # O(n^2)
        
        nums = sorted(numbers)
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] > target:
                r = r - 1
            elif nums[l] + nums[r] < target:
                l = l + 1
            elif nums[l] + nums[r] == target:
                return [l+1, r+1]
