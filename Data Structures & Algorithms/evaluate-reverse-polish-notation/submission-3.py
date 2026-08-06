class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opSet = {"+", "-", "*", "/"}
        

        for tok in tokens:
            if tok not in opSet:
                stack.append(tok)
            elif tok in opSet:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                if tok == "+":
                    stack.append(operand1 + operand2)
                elif tok == "-":
                    stack.append(operand1 - operand2)
                elif tok == "*":
                    stack.append(operand1 * operand2)
                elif tok == "/":
                    if operand2 == 0:
                        stack.append(0)
                    else:
                        stack.append(operand1 / operand2)

        return int(stack[-1])
            