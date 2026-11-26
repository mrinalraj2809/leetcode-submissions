class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # left = 0
        # max_value = -float('inf')
        # result = []
        # for right in range(len(nums)-k+1):
        #     prev_max = max(nums[right:right+k])
        #     result.append(prev_max)
        # return result
        dq = deque()
        result = []

        for right in range(len(nums)):

            # 1. Remove indices outside the current window
            while dq and dq[0] <= right - k:
                dq.popleft()

            # 2. Remove smaller elements from the right
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            # 3. Add the current index
            dq.append(right)

            # 4. Record the maximum when the window is full
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result