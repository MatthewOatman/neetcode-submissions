class Solution:

    def binarySearch(self, numbers: list[int], target: int) -> bool:
            l, r = 0, len(numbers) - 1
            while l <= r:
                m = (l + r) // 2
                if target < numbers[m]:
                    r = m - 1
                elif target > numbers[m]:
                    l = m + 1
                else:
                    # Found the number
                    return True        
            return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
            This problem can obviously code the brute force solution which is just loopig through each row and performing binary search on each. This would O(m*logn) solution
        '''
        # # Brute Force Solution:
        # for row in matrix:
        #     if self.binarySearch(row, target):
        #         return True
        # return False

        # Fast solution 

        # First we need to figure out what row our target can be in before applying binary search


        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            row = (top + bottom) // 2
            # This means we move the top pointer down
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                return self.binarySearch(matrix[row], target)

        return False
        










