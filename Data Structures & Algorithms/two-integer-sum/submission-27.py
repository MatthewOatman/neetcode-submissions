class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        One thing that immediately strikes me in the problem description is how we are dealing with indices and the specific equation. 
        nums[j] = target - nums[i]
        [4, 5, 6]
        target = 10

        first check if the length is 2 then we return 0,1
        then we can iterate through the list check the condition to calculate nums[i] and check if in set if so, return then add. add the number to a set 
        '''


        if len(nums) == 2:
            return [0, 1]

        idx = {}

        for i in range(len(nums)):
            val = target - nums[i]
            if val in idx:
                return [idx[val], i]
            idx[nums[i]] = i
        

