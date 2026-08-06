class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        What I am thinking is that we go through each of the heights and then add the height to the stack 

        keep track in a tuple (start, height)


        so say that we are traversing forward in this problem

        we start be looking at the first height we see it as 7
        so the max is simply 7

        next we look at 1. The largest rectangle can either be the first column, 7, the second column 1, or the combination of both on the horizontal 2. 

        Next we get to 7 again but this time even though it is equal we have a larager possibility of constructing a larger area. 
        We have the vertical column, the bottom row that got a new value to 3, and the forming bottom two rows. 


        Thus I feel we need to store some data associated with each of the largest areas


        compute bottom area between two rectangles as 
        min(heights left and heights right) * diff b/w indexes
        This is what we can store and use to construct on the next one along with the height, however, the cols we can simply just 



        we can create a stack and store the maximum size per each of the columns as we propogate. To calculate the max rectangle size we can use the current indexes height the previous maximum

        res = [7, 2]

        the area of the rectangle is essentially height * (right - left + 1)

        the height per index is the maximum between the 
        - its hieght
        - 
        
        maybe we simply store the max height between
        


        After viewing the submission description, this is essentially a monotonic stack solution where we keep the stack as the collection of the bars in increasing height order where each stored item is the earliest index where the height can start. When we get a new height that is less than the top of the stack, this means that the taller bar on top can't extend further to the right so we pop it and compute the area

        '''


        # What if we had a tuple (left index, height)
        stack = [] # (left, height)
        maxArea = 0


        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                left, h = stack.pop()
                maxArea = max(maxArea, h * (i - left))
                start = left

            stack.append((start,height))

        # iterate through the remaining
        while stack:
            left, h = stack.pop()
            maxArea = max(maxArea, h * (len(heights) - left))

        return maxArea

        


            


            