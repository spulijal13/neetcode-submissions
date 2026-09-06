class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        min_element = nums[0]

        while start <= end:
            if nums[start] < nums[end]:
                min_element = min(min_element, nums[start])
                break
            
            mid = (start + end) // 2

            min_element = min(min_element, nums[mid])
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        
        return min_element

