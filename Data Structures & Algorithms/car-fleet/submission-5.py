class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = list(zip(position, speed))
        cars.sort(reverse=True)  # sort by position descending
        
        stack = []

        for p, s in cars:
            time = (target - p) / s

            # if stack empty OR this car takes longer than fleet ahead
            if not stack or time > stack[-1]:
                stack.append(time)
            # else: it merges, so do nothing

        return len(stack)