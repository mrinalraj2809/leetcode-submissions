class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = []
        # for i in range(len(nums)):
        #     res.append(math.prod(nums[0:i]) * math.prod(nums[i+1:len(nums)]))
        # return res

        # Case 1: If 1 zero
        # Case 2: If more than 1 zero
        # Case 3: If no zero

        count_zero = 0
        val = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                count_zero = count_zero+1
            else:
                val = val * nums[i]
        
        res = []
        for i in range(len(nums)):
            if count_zero >=2: 
                res.append(0)
            elif count_zero == 1:
                output_val = val if nums[i] == 0 else 0
                res.append(output_val)
            else:
                res.append(int(val/nums[i]))
        return res

