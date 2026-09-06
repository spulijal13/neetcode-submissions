class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}

        for ind, num in enumerate(nums):
            maps[num] = ind

        for ind, num in enumerate(nums):
            difference = target - num

            if difference in maps and maps[difference] != ind:
                return [ind, maps[difference]]