class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '}': '{', 
            ']': '[',
            ')': '(' 
        }

        stack = []

        for c in s:
            if c in brackets.values():
                stack.append(c)
            else:
                if len(stack) < 1 or brackets[c] != stack[-1]:
                    return False
                stack.pop()

        return len(stack) == 0