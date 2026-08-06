class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # this is O(N) and gets the time
        def simulate(piles, k):
            time = 0

            for pile in piles:
                time += math.ceil(pile / k)

            return time
        
        # given the hours and want to find optimal rate for consumption

        # edge case
        if not piles:
            return 0

        # brute force would be to start k at 1 and simulate calculating time and increment rate
        # until you achieve the same amount of time to consume the bananas.
        # this is O(M x N) where M is the number of piles and N is the max number bananas

        # base case O(N)
        if len(piles) == h:
            return max(piles)

        # the time it takes koko to eat a pile of x bananas is x/k
        # upper bound is k = 1 for total num bananas or n
        # we can use this lower bound of the max and the upper bound to do a binary search for the optimal number and comparing it to the target

        lower = 1
        upper = max(piles)

        best_speed = upper

        while lower <= upper:
            middle = (lower + upper) // 2
            # simulate the bananas
            time = simulate(piles, middle)

            if time <= h:
                # Finished in time save this speed
                best_speed = middle
                # but can find a potentially slower rate
                upper = middle - 1
            else: 
                lower = middle + 1


        return best_speed
                



        



        
        

