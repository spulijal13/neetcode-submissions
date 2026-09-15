class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        begin = 0
        end = len(numbers) - 1

        while begin < end:
            if numbers[end] + numbers[begin] == target:
                return [begin + 1, end + 1]
            elif numbers[begin] + numbers[end] < target:
                begin += 1
            else:
                end -= 1