class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
            This seems like another monotonic stack problem where the cars positions and rates of travel are dependent eventually on the cars in front of them.

            Questions:
            - Are the positions in order at all?
            - If so it would allow to go in reverse and find the first car to reach the end
            

            I have an idea, if we sort the arrays by position, then use the position sort to sort the speed with lambda, then we can get the postions and speed for each of the cars in the order of positons. Can look at the last position, see how fast it gets to the target with equation ((target - position) / speed) then save that speed and determine if the car behind will catch up or not. If so it will have the same destination time. 


            Ex: 
            pos = [4,1,0,7]
            speed = [2, 2, 1, 1]

        sorted:             target = 10
            [0, 1, 2, 7]
            [1, 2, 1.5, 1]

        time = (target - position) / speed
        stack = [10, 4.5, 3, 3]

        convert to a set and then return the length of the set

        '''

        # sort the pos and the speed in descending order
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for pos, spd in cars:
            # compute the time to finish
            time = (target - pos) / spd
            if stack and time < stack[-1]:
                continue
            else:
                stack.append(time)
        
        unique = len(set(stack))

        return unique
                


