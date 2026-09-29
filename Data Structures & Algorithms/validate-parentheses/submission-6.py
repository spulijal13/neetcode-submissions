class Solution:
    def isValid(self, s: str) -> bool:
        check = {"]":"[", ")":"(", "}":"{"}
        stack = []

        for val in s:
            print(val)
            if val in check:
                if len(stack) == 0 or check[val] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(val)
        
        return True if len(stack) == 0 else False