class Solution:
    def __init__(self):
        self.i = 0

    def reverseParentheses(self, s: str) -> str:
        
        stack = ''

        while self.i < len(s):

            if s[self.i] == '(':
                self.i += 1
                stack += self.reverseParentheses(s)
            elif s[self.i] == ')':
                self.i += 1
                return stack[::-1]
            else:
                stack += s[self.i]
                self.i += 1
        
        return stack