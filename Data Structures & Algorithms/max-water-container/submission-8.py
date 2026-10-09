class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxim = -1
        # print(l, r)
        while l < r:
            a = min(heights[l] , heights[r])
            b = (r - l)
            maxim = max(a*b, maxim)
            # if a*b > maxim:
            #     maxim = a * b
            if heights[l] <= heights[r]:
                l += 1
            else : 
                r -= 1
        return maxim
        # maxim = 0
        # for i in range(len(heights)-1):
        #     for j in range(i+1, len(heights)):
        #         if min(heights[i], heights[j]) * (j - i) > maxim:
        #             maxim = min(heights[i], heights[j]) * (j - i)
        # return maxim