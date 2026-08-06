class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        my_set = {}

        for num in nums:
            if num in my_set:
                return True
            my_set[num] = 1
        
        return False
    

        