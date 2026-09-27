class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        begin = 0
        end = 0
        maxString = 0

        while end < len(s):
            count[s[end]] += 1

            if count[s[end]] > 1:
                while count[s[end]] > 1:
                    count[s[begin]] -= 1
                    begin += 1
            
            maxString = max(maxString, end - begin + 1)
            end += 1

        return maxString