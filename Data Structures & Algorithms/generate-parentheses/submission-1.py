class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        

        def backtrack(openN, closeN):
            # Base case finished
            if openN == closeN == n:
                res.append("".join(stack))

            # open num < n (open paren add)
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()
            
            # closeN < openN (close paren add)
            if closeN < openN:
                # need to add the close parent to something
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()


        backtrack(0,0)
        return res