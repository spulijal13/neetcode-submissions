class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxLength = 0
        l = 0
        maxC = 0

        for r in range(len(s)):
            count[s[r]] += 1
            maxC = max(maxC, count[s[r]])

            while (r - l + 1) - maxC > k:
                count[s[l]] -= 1
                l += 1

            maxLength = max(maxLength, r - l + 1)          

        return maxLength
            