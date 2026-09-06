class Solution:
    def isValid(self, s: str) -> bool:
        OPENING_PAREN = ['[', '{', '(']
        OPPOSITE_PAREN = {']': "[", '}': '{', ')': '('}
        stack = []

        for c in s:
            if c in OPENING_PAREN:
                stack.append(c)
            else: 
                if not (c in OPPOSITE_PAREN.keys() and len(stack) > 0 and OPPOSITE_PAREN[c] == stack[-1]):
                    return False
                stack.pop()

        return len(stack) == 0