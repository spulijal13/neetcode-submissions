class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodNoZero = 1
        zero = 0

        for i in nums:
            if i == 0:
                zero += 1
            else:
                prodNoZero *= i
        
        ans = []
        for j in nums:
            if zero > 1:
                ans.append(0)
            elif zero == 1 and j == 0:
                ans.append(prodNoZero)
            elif zero == 1:
                ans.append(0)
            else:
                ans.append(prodNoZero // j)
        

        return ans

                