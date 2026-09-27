class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        begin = 0
        maxString = 0

        for end in range(len(s)):
            if s[end] in count:
                begin = max(count[s[end]] + 1, begin)
            
            count[s[end]] = end
            maxString = max(maxString, end - begin + 1)
        
        return maxString