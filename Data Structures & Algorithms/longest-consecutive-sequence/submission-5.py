class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        order = {}
        longest = 0

        for n in nums:
            order[n] = order.get(n, 0) + 1
        
        for n in nums:
            if order.get(n - 1, 0) <= 0:
                count = 0
                temp = n
                while True:
                    if order.get(temp, 0) > 0:
                        count += 1
                    else:
                        break
                    temp += 1
                longest = max(count, longest)
        

        return longest

