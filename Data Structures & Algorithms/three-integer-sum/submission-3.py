class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Notes:
            No duplicates. All triplets possible, all elements in triplets have distinct indexes
            All of the triplets must equal 0 we are also returning the values and not the indexes

        range for the constraints being 10^5 elements makes me think that there should be O(n) or O(nlogn) solution

        EX:

        [-1,0,1,2,-1,-4]

        nums[0] + nums[1] + nums[2] = -1 + 0 + 1 = 0
        nums[4] + nums[1] + nums[2] = -1 + 0 + 1 = 0
        nums[4] + nums[0] + nums[3] = -1 + -1 + 2 = 0

        output = [[-1,0,1], [-1,-1,2]]

        set() containing the elements of the tuple

        Sorting in ascending order
        [-4, -1, -1, 0, 1, 2]
              ^            ^

          since l + r < 0 
          then move l ++ because can't get greater

        sum = 1 > 0  then do we search in the bounds linearly for the last element
        '''
        res = []
        # Sort in ascending order
        nums.sort()

        for i, num in enumerate(nums):
            # Don't use the same value that has previously been looked at
            if i > 0 and num == nums[i - 1]:
                continue
            if num > 0:
                break

            # perform the two pointer two sum algorithm 
            l =  i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res




