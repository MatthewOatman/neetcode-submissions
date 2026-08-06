class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        '''

        k is essentially your hourly eating rate


        piles = [3, 10, 4, 5]

        in total with k = 2 we would have 12 hours here

        however, we can derive back, if we have h = 10 and have 4 piles, then we would have an average eating rate of 0.4 piles per hour

        lets look at given example in the question:

        piles = [1,4,3,2], h = 9

        the fastest eating rate is the max in a pile ex: k = 4 -> h = 4

        the slowest eating rate is k = 1 however that does not satisfy the alloted time. 

        so we have a range of rates 1 -> max_in_a_pile

        we check how many hours it takes for each of the rates to consume all the piles 

        we then perfrom binary search and check how long it takes to consume
        '''
        '''
        piles = [1,4,3,2], h = 9
        fastest = 1
        slowest = 1

        k = 1
        time = 6
        '''

        # Compute max rate
        fastest = max(piles)
        slowest = 1
        rate = fastest

        while slowest <= fastest:
            k = (slowest + fastest) // 2

            # Compute the hours it takes
            time = self.eatingTime(piles, k)
            if time <= h:
                rate = k
                fastest = k - 1
            elif time > h:
                slowest = k + 1

        return rate
        


    def eatingTime(self, piles, k):
        time = 0
        
        for pile in piles:
            time += math.ceil(pile / k) 

        return time





