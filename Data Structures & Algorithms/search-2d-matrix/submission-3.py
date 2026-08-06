class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(row, target):

            l, r = 0, len(row) - 1

            while l <= r:
                middle = (l + r) // 2
        
                if row[middle] == target:
                    return True
                elif row[middle] < target:
                    l = middle + 1
                else:
                    r = middle - 1

            return False

        # Check if the matrix exists
        if not matrix:
            return False

        # brute force solution is to simply loop through every row and check every item to see if the target exists
        # This is O(M*N) time complexity

        # A more efficient solution is to iterate through the rows and then compute binary search on the rows
        # this is O(m*log(n))

        # if the length is 1 then we only have one row to compute binary search on 
        if len(matrix) == 1:
            return binarySearch(matrix[0], target)
        # if the length is 2 or more, then we can use the two pointer technique

        else:
            l, r = 0, 1
            while r < len(matrix):

                if target >= matrix[l][0] and target < matrix[r][0]:
                    return binarySearch(matrix[l], target)
                else:
                    l += 1
                    r += 1
            
            # check the last row if not returned already
            return binarySearch(matrix[r-1], target)





        
        