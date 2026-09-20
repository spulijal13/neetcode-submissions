class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"}":"{", ")":"(", "]":"["}

        for value in s:
            if value in brackets.keys():
                if not stack:
                    return False
                elif stack[-1] != brackets[value]:
                    return False
                else:
                    stack.pop()
                
                continue

            stack.append(value)

        return not stack