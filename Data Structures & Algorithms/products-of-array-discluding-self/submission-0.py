class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        suff = []
        product = 1
        for i in range(len(nums)):
            pref.append(product)
            product *= nums[i]

        product = 1
        for j in range(len(nums) - 1, -1, -1):
            suff.append(product)
            product *= nums[j]
        
        ans = []
        length = len(nums)
        for k in range(length):
            ans.append(suff[length - 1 - k] * pref[k])
        
        return ans

            