class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for i in nums:
            counts[i] += 1

        bucket = [[] for j in range(len(nums) + 1)]
        for key, value in counts.items():
            bucket[value].append(key)
        
        ans = []
        for m in range(len(nums), 0, -1):
            for l in bucket[m]:
                ans.append(l)
                if len(ans) == k:
                    return ans
        
        return ans
            
