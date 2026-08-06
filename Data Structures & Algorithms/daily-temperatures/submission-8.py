class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        '''

        Notes:

        Apparently this is a very hard problem for others and learning monotonic stack is beneficial for understanding this problem.
        Context Clues:
        - Looking for something in the future
        - Number of days rather than the temperature (Looking for index)

        example
        temps = [33, 28, 32, 64, 135, 42, 75]
        output = [3, 1 , 1, 1, 0, 1, 0]


        [33, 32]
        '''

        

        # Brute force

        # Interesting approach where it is better to use the indexes to compare the counts instead of simply incrementing a counter.

        # res = [0] * len(temperatures)

        # for i in range(len(temperatures)):

        #     for j in range(i + 1, len(temperatures)):

        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i
        #             break
        # return res



        # Trying the stack solution
        # forward approach

        # We can use the stack as a waiting room for numbers that don't already have a larger temp that came

        # temps = [30,38,30,36,35,40,28]
        # stack = [1]
        #   res = [1, 0, 0, 0, 0, 0, 0]

        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # We found a larger number
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
    
            stack.append(i)


        return res



        