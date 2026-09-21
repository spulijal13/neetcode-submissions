class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        char = set()

        for n in nums:
            if n in char:
                return True
            
            char.add(n)
        
        return False