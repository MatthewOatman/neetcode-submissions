class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        # the brute force approach would be O(n^3).

        # O(n^2) solution by looping through all of the 
        # indexes then perform two sum on rest target variables
        # problem with this is receiving duplicate triplets
        # multiple ways to compute the two sum for each 3rd index



        # Sort the array and iterate through while computing the two sum on each. 
        # Remove the duplicates by incrementing the pointers if the value is the same as the last

        nums.sort()

        res = []

        for i, a in enumerate(nums):
            # all the following must be positive so no three sum can be found
            if a > 0:
                break

            # skip the repeats
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


