class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                p_ind, p_height = stack.pop()
                max_area = max(max_area, p_height * (index - p_ind))
                start = p_ind
            stack.append((start, height))
        
        n = len(heights)
        for index, height in stack:
            max_area = max(max_area, height * (n - index))
        
        return max_area