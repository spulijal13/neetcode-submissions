class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        total_product = 1

        for n in nums:
            if n != 0:
                total_product *= n
            else:
                zero_count += 1
        
        n = len(nums)
        output = [0] * n

        if zero_count > 1:
            return output

        for i in range(n):
            if zero_count > 0:
                if nums[i] == 0:
                    output[i] = total_product
                
            else:
                output[i] = total_product // nums[i]

        
        return output

            