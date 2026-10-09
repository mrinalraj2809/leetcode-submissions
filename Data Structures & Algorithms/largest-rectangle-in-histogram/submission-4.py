class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxim_area = 0
        stack = []  # stores (index, height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxim_area = max(maxim_area, height * (i - idx))
                start = idx
            stack.append((start, h))
        
        for idx, height in stack:
            maxim_area = max(maxim_area, height * (len(heights) - idx))
            
        return maxim_area