class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        if not height:
            return water
        
        left = [0] * len(height)
        right = [0] * len(height)

        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(left[i-1], height[i])
        
        right[-1] = height[-1]
        for j in range(len(height) - 2, -1, -1):
            right[j] = max(right[j + 1], height[j])
        
        for k in range(len(height)):
            water += min(left[k], right[k]) - height[k]
        
        return water

