class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        print(nums)
        counter = 1
        max_counter = -1
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                counter = counter + 1
            else:
                if counter > max_counter:
                    max_counter = counter
                counter = 1
        if counter > max_counter:
            max_counter = counter
        return 0 if len(nums) == 0 else max_counter 
        