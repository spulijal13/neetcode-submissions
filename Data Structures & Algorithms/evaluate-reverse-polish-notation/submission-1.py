class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []

        for t in tokens:
            if t == "+" or t == "-" or t == "*" or t == "/":
                first = numbers.pop()
                second = numbers.pop()

                if t == "+":
                    numbers.append(first + second)
                elif t == "-":
                    numbers.append(second - first)
                elif t == "*":
                    numbers.append(first * second)
                elif t == "/":
                    numbers.append(int(second / first))
            else:
                numbers.append(int(t))
        

        return numbers[0]

        