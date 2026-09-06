class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}

        for l in s1:
            count[l] = 1 + count.get(l, 0)
        
        k = len(s1)
        j = len(s2)

        if j < k:
            return False
        
        f = 0
        r = 0
        ans = {}
        while r < j:
            print
            ans[s2[r]] = 1 + ans.get(s2[r], 0)
            if r - f + 1 >= k:
                if ans == count:
                    return True

                ans[s2[f]] -= 1
                if ans[s2[f]] == 0:
                    ans.pop(s2[f])
                f += 1
            r += 1
        
        return False
        
