class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        present = set()

        for i in nums:
            present.add(i)
        
        longest = 0

        for j in nums:
            if j - 1 not in present:
                count = 1
                while j + count in present:
                    count += 1
                
                longest = max(longest, count)
        
        return longest


        # then start at some list value then check if your value is part of already longest ubs sequence if it is then skip, 
        # otherwise run it and if it reaches the original longest one then append onto that, but that is not really 
        #saving time. 