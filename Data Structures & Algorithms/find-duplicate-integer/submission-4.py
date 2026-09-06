class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow, fast = 0, 0
        prev_slow, prev_fast = 0, 0
        n = len(nums)

        while True:
            if nums[slow] == nums[fast] and fast != slow:
                return nums[slow]
            
            if nums[prev_slow] == nums[fast] and fast != prev_slow:
                return nums[fast]
            
            if nums[prev_fast] == nums[slow] and slow != prev_fast:
                return nums[slow]
            
            prev_slow = slow
            prev_fast = fast
            slow += 1
            fast += 2

            if slow >= n:
                slow = 0
            
            if fast >= n:
                fast = 0
        
        return 0