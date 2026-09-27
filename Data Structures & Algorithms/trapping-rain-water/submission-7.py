class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        if not height:
            return water
        
        l = 0
        r = len(height) - 1
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                water += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                water += rightMax - height[r]
        
        return water
        


