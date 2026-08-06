class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(n) solution where we iterate through a list once over and each time we get to an element we can add it to a set and see if the item is already in a set
        # Add the first element of the array to the list after checking the first base condition. Then we iterate through the array starting at index 1 and going to the end then in the loop we will check if the number is in dup set if so return true if not continue, if we get through the loop and nothing is found then we can return false. 

        # Edge case 1: if len nums is 0 or 1 then we return false. 


        length = len(nums)
        if length == 0 or length == 1:
            return False

        dup = set()
        dup.add(nums[0])

        for i in range(1, length):
            if nums[i] in dup:
                return True
            dup.add(nums[i])
        
        return False


    