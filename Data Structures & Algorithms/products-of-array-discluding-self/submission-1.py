class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        My immediate thought is that the very brute force answer is to do it in O(n^2) time where we loop through the array for as many times as elements and simply create a running product as we go. 

        nums = [1,2,4,6]
        i = 
        curr_prefix = 1

        prefix = [1, 1, 1, 1]



        prods = [48, 24, 12, 8]
        '''


        prefix = [1] * len(nums)
        curr_prefix = 1

        # nums = [1,2,4,6]
        # prefix = [1,1,2,8]
        # curr = 8
        # i = 3

        # Create the prefix array
        for i in range(1, len(nums)):
            curr_prefix *= nums[i - 1]
            prefix[i] *= curr_prefix


        suffix = [1] * len(nums)
        curr_suffix = 1

        # Create the suffix array
        # nums = [1,2,4,6]
        # suffix = [1,24,6,1]
        # curr = 24
        # i = 0


        for i in range(len(nums) - 2, -1, -1):
            curr_suffix *= nums[i + 1]
            suffix[i] *= curr_suffix

        res = []
        for i in range(len(prefix)):
            res.append(prefix[i] * suffix[i])

        return res







