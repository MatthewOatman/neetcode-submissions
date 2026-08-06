class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        '''

        zero is the default

        example
        temps = [33, 28, 32, 64, 135, 42, 75]
        output = [3, 1 , 1, 1, 0, 1, 0]
        '''

        # Brute force

        res = []

        for i, n1 in enumerate(temperatures):
            count = 0
            found = False
            for j, n2 in enumerate(temperatures[i+1:]):
                count += 1
                if n2 > n1: # Condition where we found larger
                    res.append(count)
                    found = True
                    break

            if not found:
                res.append(0)

        return res
        