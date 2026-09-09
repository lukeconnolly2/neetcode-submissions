class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        OPERATORS = ['+', '-', '*', '/']

        for i in range(len(tokens)):
            if tokens[i] in OPERATORS:
                res = None
                y = stack.pop()
                x = stack.pop()

                if tokens[i] == '+':
                    res = x + y
                elif tokens[i] == '-':
                    res = x - y
                elif tokens[i] == '*':
                    res = x * y
                else:
                    res = int(x / y)

                stack.append(res)

            else: 
                stack.append(int(tokens[i]))

        return stack.pop()