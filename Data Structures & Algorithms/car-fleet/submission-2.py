class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        length = len(position)
        reached = [0] * length

        combined = sorted([(position[i], speed[i]) for i in range(length)])

        for i in range(length):
            reached[i] = (target - combined[i][0]) / combined[i][1]
        
        max_val = reached[-1]
        for i in range(length):
            if reached[length - i - 1] > max_val:
                max_val = reached[length - i - 1]
            elif reached[length - i - 1] < max_val:
                reached[length - i - 1] = max_val
        
        

        reached_unique = set(reached)
        return len(reached_unique)
            
        
        