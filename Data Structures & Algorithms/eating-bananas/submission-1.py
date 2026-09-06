import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        min_time = end

        while start <= end:
            k = (start + end) // 2

            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / k)
            
            if total_time <= h:
                min_time = k
                end = k - 1
            else:
                start = k + 1

        return min_time