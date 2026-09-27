class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowered = s.strip().lower()

        left = 0
        right = len(lowered) - 1

        while left < right:
            while left < right and not lowered[left].isalnum():
                left += 1
            
            while left < right and not lowered[right].isalnum():
                right -= 1
            
            
            if lowered[left] != lowered[right]:
                return False
            
            left += 1
            right -= 1
        
        return True