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

        for row in matrix:
            if self.binarySearch(row, target):
                return True


        return False
            