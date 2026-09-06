class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        contains = {}

        for i, val in enumerate(nums):
            contains[val] = i
        

        for j, val in enumerate(nums):
            i = contains.get(target - val, -1)

            if i != -1 and i != j:
                return [min(i,j), max(i, j)]