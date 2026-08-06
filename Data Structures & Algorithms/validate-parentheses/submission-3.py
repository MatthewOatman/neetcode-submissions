class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for c in s:
            if c in ['(','[','{']:
                stk.append(c)
            elif c == '}' and stk and stk[-1] == "{":
                stk.pop()
            elif c == ']' and stk and stk[-1] == "[":
                stk.pop()
            elif c == ')' and stk and stk[-1] == "(":
                stk.pop()
            else:
                return False


        return not stk
