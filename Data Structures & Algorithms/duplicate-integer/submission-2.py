class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for v in nums:
            hash_map[v] = hash_map.get(v, 0) + 1

            if hash_map[v] > 1:
                return True
        
        return False
