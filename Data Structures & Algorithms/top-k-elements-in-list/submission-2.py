class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        heap = []

        for key, value in count.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)
            
        return [tup[1] for tup in heap]

