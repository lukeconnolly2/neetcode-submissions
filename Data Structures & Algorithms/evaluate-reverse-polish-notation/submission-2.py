class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        OPERATORS = ['+', '-', '*', '/']

        for i in range(len(tokens)):
            currElement = tokens[i]

            if currElement not in OPERATORS:
                stack.append(int(currElement))
            else: 
                y = stack.pop()
                x = stack.pop()
                result = None

                if currElement == '+':
                    result = x + y
                elif currElement == '-':
                    result = x - y
                elif currElement == '*':
                    result = x * y
                else: 
                    result = int(x / y)
                
                stack.append(result)
        
        return stack.pop()
            
