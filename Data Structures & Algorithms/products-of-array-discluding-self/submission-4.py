class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0

        for n in nums:
            if n == 0:
                zeros += 1
            else:
                product *= n

        ans = []

        for i, n in enumerate(nums):
            value = 0
            if zeros > 1:
                value = 0
            elif zeros == 1:
                if n == 0:
                    value = product
                else:
                    value = 0
            else:
                value = product // n


            
            ans.append(value)
        
        return ans