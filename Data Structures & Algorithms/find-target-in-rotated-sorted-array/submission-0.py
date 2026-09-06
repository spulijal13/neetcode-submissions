class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        min_element = nums[0]
        min_index = 0

        while start <= end:
            if nums[start] <= nums[end]:
                if nums[start] < min_element:
                    min_element = nums[start]
                    min_index = start
                break
            
            mid = (start + end) // 2

            if nums[mid] < min_element:
                min_element = nums[mid]
                min_index = mid

            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid
        
        start = 0
        length = len(nums)
        end = length - 1

        while start <= end:
            mid = (start + end) // 2

            check_index = (mid + min_index) % length

            if target == nums[check_index]:
                return check_index
            elif target > nums[check_index]:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1
