class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        total = []
        stack = []

        for i in range(len(position)):
            total.append((position[i], (target - position[i]) / speed[i]))
        
        total.sort(reverse=True)

        for pos, time in total:
            if stack and time <= stack[-1]:
                continue
            
            stack.append(time)
    

        return len(stack)
        
