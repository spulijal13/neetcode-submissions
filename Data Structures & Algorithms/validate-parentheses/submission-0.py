class Solution:
    def isValid(self, s: str) -> bool:
        parens = []
        end = 0

        for c in s:
            if c == "(":
                parens.append("(")
                end += 1
            elif c == "[":
                parens.append("[")
                end += 1
            elif c == "{":
                parens.append("{")
                end += 1
            elif c == "}" or c == ")" or c == "]":
                if end == 0:
                    return False
                
                if c == "}":
                    if parens[end-1] == "{":
                        parens.pop()
                        end -= 1
                    else:
                        return False
                
                elif c == ")":
                    if parens[end-1] == "(":
                        parens.pop()
                        end -= 1
                    else:
                        return False
                
                elif c == "]":
                    if parens[end-1] == "[":
                        parens.pop()
                        end -= 1
                    else:
                        return False
        if end == 0:
            return True
        return False
