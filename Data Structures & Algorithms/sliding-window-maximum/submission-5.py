class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        current = {}
        ans = []
        l = 0
        heap = []

        for r in range(len(nums)):
            heapq.heappush(heap, -nums[r])
            current[nums[r]] = 1 + current.get(nums[r], 0)

            if r - l + 1 < k:
                continue

            while -heap[0] not in current or current[-heap[0]] == 0:
                heapq.heappop(heap)
            
            ans.append(-heap[0])

            current[nums[l]] -= 1
            l += 1
            r += 1
        
        return ans
            
            
