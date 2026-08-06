class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        '''
        We need to find an equation to be able to compute the wrap of a specific index

        [1,2,|3|,4,5,6]
        [6,1,2,3,4,5] # rotated once
        [5,6,|1|,2,3,4]
        [4,5,6,1,2,3]

        we can compute how many times the array has been rotated by from this patter

        last element = nums[-1]
        rotations = len(nums) - nums[-1]
        '''


        # what if we used binary search to find the minimum here

        '''
        [3,4,5,6,1,2]

        left = 3
        right = 3
        mid = 4

        '''

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # Min must be to the right of mid
                left = mid + 1
            else:
                # Min is mid itself, or to its left
                right = mid

        pivot = left  # Index of the smallest element



        # --- PASS 2: Determine search range & Binary Search ---
        # Check if target belongs in the right sorted portion
        if nums[pivot] <= target <= nums[-1]:
            l, r = pivot, len(nums) - 1
        else:
            l, r = 0, pivot - 1

        # Standard Binary Search
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        return -1




        '''
        [3,4,5,6,1,2]

        l = 0   nums[l] = 3
        r = 5   nums[r] = 2
        m = 2   nums[m] = 5

        if nums[l] < nums[mid] - means that strictly increasing on that left range
            if target > nums[mid] or target < nums[l]
                l = mid + 1
            else:
                r = mid - 1
        else: - means that strictly increasing on the right range
            if target < nums[mid] or target > nums[r]
                r = mid - 1
            else
                l = mid + 1
        
        if target == nums[mid]:
            return mid


        '''


    

