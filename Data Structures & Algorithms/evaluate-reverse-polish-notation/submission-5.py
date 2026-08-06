class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        operand = a number
        operator = an equation

        division always truncates towards zero int(a / b)

        '''

        operators = {'+', '-', '*', '/'}
    
        stack = []


        for token in tokens:
            if token in operators:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())

                if token == "+":
                    result = operand1 + operand2
                elif token == "-":
                    result = operand1 - operand2
                elif token == "/":
                    result = int(operand1 / operand2)
                elif token == "*":
                    result = operand1 * operand2

                stack.append(result)
            
            else: # not an operator
                stack.append(token)

        return int(stack[-1])
