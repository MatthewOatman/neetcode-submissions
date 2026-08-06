class Solution:
    def isValid(self, s: str) -> bool:
        
        ''' 
        Examples


        ((())())

        {([]{[()]}())}

        map that maps the open symbol to the close symbol for simple checking if it is valid or not


        stack = []


        ((()))

        if 
        '''

        close_to_open = {")" : "(", "}" : "{", "]" : "["}

        stack = []

        for symbol in s:
            # closed symbol
            if symbol in close_to_open:
                if stack and stack[-1] == close_to_open[symbol]:
                    stack.pop()
                else:
                    return False

            else: # Add the open symbol to the stack
                stack.append(symbol)

        return True if not stack else False
