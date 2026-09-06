class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        total = 1

        for n in nums:
            if n != 0:
                total *= n
            else:
                zeroes += 1
        
        output = [0] * len(nums)

        if zeroes > 1:
            return output
        
        for i, v in enumerate(nums):
            if zeroes > 0:
                if v == 0:
                    output[i] = total
            else:
                output[i] = total // v
            
        return output
            