class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set(['+', '-', '*', '/'])
        stack = []

        for val in tokens:
            if val.strip() in operations:
                second = stack.pop()
                first = stack.pop()

                if val == '+':
                    stack.append(first + second)
                elif val == '-':
                    stack.append(first - second)
                elif val == '*':
                    stack.append(first * second)
                elif val == "/":
                    stack.append(int(first / second))
            else:
                stack.append(int(val))
        
        return stack[0]
        