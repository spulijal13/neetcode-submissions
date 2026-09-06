class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        count = 1

        for ind, temp in enumerate(temperatures):
            print(ind, temp)
            print(stack)
            if not stack:
                stack.append((temp, ind))
            elif temp <= stack[-1][0]:
                stack.append((temp, ind))
            elif temp > stack[-1][0]:
                while stack:
                    if stack[-1][0] < temp:
                        val = stack.pop()
                        answer[val[1]] = ind - val[1]
                        count += 1
                    else:
                        break
                stack.append((temp, ind))
                count = 1
            print(answer)
        
        return answer
                
            



    
            

