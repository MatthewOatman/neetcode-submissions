class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # Water is equal to the area. Thus, we have width = difference in indexes, j - i
        # and the height is max(heights[i], heights[j])

        # Since we are using two indexes, my mind immediately goes to two pointers

        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            # compute our widths
            width = r - l
            height = min(heights[l], heights[r])

            print("l: ", l)
            print("r: ", r)
            print("width: ", width)
            print("height: ", height, "\n")

            area = width * height
            res = max(area, res)
            
            # now we need to figure out how to modify the pointers to max the area
            # move the shorter height value in 
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return res