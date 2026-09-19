class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicates = set()
        count = 0
        begin = 0

        for end in range(len(s)):
            while s[end] in duplicates:
                duplicates.remove(s[begin])
                begin += 1
            duplicates.add(s[end])
            count = max(count, end - begin + 1)
        
        return count


