class Solution:
    def trap(self, height: List[int]) -> int:
        # if len(height) < 2:
        #     return 0
        # l = 0
        # r = 1
        # while l < r:
        #     min(maxH, height[l])
        #     l += 1
        #     r += 1
        left_right_heights = []
        maxim = 0
        for i in range(len(height)):
            maxim = max(maxim, height[i])
            left_right_heights.append([maxim])
        maxim = 0
        for i in range(len(height)-1, -1, -1):
            maxim = max(maxim, height[i])
            left_right_heights[i].append(maxim)

        total_water_trapped = 0
        for i in range(len(height)):
            if 0 in left_right_heights[i]:
                trap = 0
            else:
                left = left_right_heights[i][0]
                right = left_right_heights[i][1]
                curr = height[i]
                trap = min(left, right) - curr
            total_water_trapped += trap
        return total_water_trapped
        