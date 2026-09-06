class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            if hash_map.get(num, 0) > 0:
                return True
            
            hash_map[num] = 1
        
        return False
