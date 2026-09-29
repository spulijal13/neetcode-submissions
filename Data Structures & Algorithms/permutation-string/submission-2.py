class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        k = len(s1)
        r = k - 1

        if len(s2) < k:
            return False
        
        countSub = {}
        countString = {}

        for c in s1:
            countSub[c] = countSub.get(c, 0) + 1
        
        for d in s2[l:r]:
            countString[d] = countString.get(d, 0) + 1

        while r < len(s2):
            countString[s2[r]] = 1 + countString.get(s2[r], 0)

            if countSub == countString:
                return True
            countString[s2[l]] -= 1
            if countString[s2[l]] <= 0:
                countString.pop(s2[l], None)
            
            l += 1
            r += 1
                
        
        return False
            



