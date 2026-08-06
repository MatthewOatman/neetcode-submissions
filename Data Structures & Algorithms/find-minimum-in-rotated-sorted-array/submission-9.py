class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(N) solution is:
        # return min(nums)

        # But we need to compute binary search somehow
        # binary search primarily works by using a two pointer technique on a sorted list
        # these arrays are sorted but are shifted so we need to use math to get the most accurate index


        # Need to find a way to get the starting 1 value 

        # [3,4,5,6,1,2]

        l, r = 0, len(nums) - 1
        minimum = nums[0]

        while l <= r:

            # If the current sub-array is already perfectly sorted, 
            # the leftmost element is the smallest.
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
                break

            middle = (l + r) // 2

            # Always check if the current middle is the new minimum
            minimum = min(minimum, nums[middle])

            # If the left half is sorted, the pivot (minimum) MUST be in the right half.
            if nums[middle] >= nums[l]:
                l = middle + 1
            # Otherwise, the right half is sorted, so the pivot MUST be in the left half.
            else:
                r = middle - 1

        return minimum

        

        # we can get the index of the lowest value and the highest value with the starting value


        # 4 5 0 1 2 3
        # l = 0
        # r = 5
        # m = 2 (0)

        # if m < r:
        #     take the left side
        # elif m > r
        #     take the right side
        # else:
        #     return m