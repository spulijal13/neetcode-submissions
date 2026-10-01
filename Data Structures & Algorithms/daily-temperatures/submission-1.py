class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                someI, someVal = stack.pop()

                ans[someI] = i - someI
            
            stack.append((i, v))
        
        return ans


