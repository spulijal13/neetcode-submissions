class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {'(':')', '{':'}', '[':']'}

        for par in s:
            if par in key.keys():
                stack.append(par)
            else:
                
                if stack and key[stack[-1]] == par:
                    stack.pop()
                else:
                    return False
        

        return True if not stack else False
            
