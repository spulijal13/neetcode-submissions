class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        right = [len(heights)] * len(heights)
        left = [-1] * len(heights)
        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                curVal = stack.pop()
                right[curVal] = i
            
            stack.append(i)
        
        for j in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[j]:
                curVal = stack.pop()
                left[curVal] = j
            
            stack.append(j)

        ans = 0
        for k in range(len(heights)):
            width = right[k] - left[k] - 1
            ans = max(ans, width * heights[k])
        
        return ans