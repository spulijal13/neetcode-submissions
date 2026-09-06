class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        bucket = [[] for i in range(len(nums) + 1)]

        for (num, freq) in count.items():
            bucket[freq].append(num)
        
        ans = []
        
        for freq in range(len(bucket) - 1, 0, -1):
            for val in bucket[freq]:
                ans.append(val)

                if len(ans) == k:
                    return ans

        return ans
        
        

        