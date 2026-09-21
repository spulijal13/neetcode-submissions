class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = defaultdict(int)

        for i, v in enumerate(nums):
            goal = target - v
            if goal in count:
                return [count[goal], i]
            
            count[v] = i
        
        return []

