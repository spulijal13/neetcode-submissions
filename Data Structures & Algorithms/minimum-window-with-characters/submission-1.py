class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        countS = {}
        countT = {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        l = 0
        minLen = float("inf")
        minSub = ""
        need = len(countT.keys())
        have = 0

        for r in range(len(s)):
            if s[r] in countT:
                countS[s[r]] = 1 + countS.get(s[r], 0)
                if countS[s[r]] == countT[s[r]]:
                    have += 1
            
            while have == need:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    minSub = s[l:r + 1]
                
                if s[l] in countT:
                    countS[s[l]] -= 1

                    if countS[s[l]] < countT[s[l]]:
                        have -= 1
                
                l += 1
        
        return minSub
            
                    
            
            
                    

            
            
                
            