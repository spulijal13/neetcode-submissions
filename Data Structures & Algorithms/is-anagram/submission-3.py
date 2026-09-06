class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashed = {}

        for sl in s:
            hashed[sl] = hashed.get(sl, 0) + 1

        for tl in t:
            if tl not in hashed:
                return False
            
            hashed[tl] -= 1

            if hashed[tl] < 0:
                return False
        
        return True