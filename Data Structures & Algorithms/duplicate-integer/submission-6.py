class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # create dictionary 
        # hash = {}
        # for i in nums:
        #     hash[i] = hash.get(i, 0) + 1

        #     if hash[i] == 2:
        #         return True

        # return False

        # Use a Set (implement using hashmap in python)

        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)

        return False



    

        