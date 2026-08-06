class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        ''' This problem wants me to construct binary search because of the O(logn) time complexity
        
        Binary Search has O(logn) average and O(logn) worst case

        This algorithm works by finding the left and the right pointers then finding the middle, first check that the middle is the correct value, if it is less minimize the window by making the right pointer the middle pointer, if it is greater than the middle then make the left pointer the middle pointer +1, keep doing that while l < r

'''

        '''
        EX: 
        nums = [-1,0,2,4,6,8]
        target = 4
        l = 3
        r = 4
        m = 7/2 3



        '''

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = int((l + r) / 2)

            if target == nums[m]:
                return m
            elif target < nums[m]:
                # Move the right pointer to m
                r = m - 1
            else:
                # move the left pointer
                l = m + 1

        return -1




