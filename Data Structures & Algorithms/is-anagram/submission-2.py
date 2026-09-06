class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash1 = {}
        hash2 = {}

        for sl in s:
            hash1[sl] = hash1.get(sl, 0) + 1

        for tl in t:
            hash2[tl] = hash2.get(tl, 0) + 1
        
        return hash1 == hash2