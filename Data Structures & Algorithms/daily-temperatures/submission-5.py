class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # This is the 0(n^2) solution
        # n = len(temperatures)
        # res = [0] * n

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i
        #             break

        # return res


        # Monotonic Stack
        res = [0] * len(temperatures)
        stack = [] # pairs (temp, index)


        for i, temp in enumerate(temperatures):
            # make sure that an element is on the stack if greater than the head
            while stack and temp > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = (i - stackIndex)
            stack.append((temp, i))

        return res


            
            







        


