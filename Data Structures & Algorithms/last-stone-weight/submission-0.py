class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pile = stones
        for i, v in enumerate(pile):
            pile[i] = -v
        heapq.heapify(pile)

        print(pile, stones)
        

        while len(pile) > 1:
            first = -heapq.heappop(pile)
            second = -heapq.heappop(pile)

            print(first, second)
            
            if second < first:
                heapq.heappush(pile, -(first - second))

        if len(pile) != 1:
            return 0
        
        return -pile[0]