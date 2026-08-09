class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
            So of course the brute force way of doing it would be to create a hash set and loop through in O(1) time adding to the set and finally seeing if the item has already been in the set however the solution is looking for a O(1) space complexity answer which means that it is looking for pointer solution



            len(nums) = n + 1
            numbers range [1, n]. 
            Thus the range of n elements and one of the elements in the range is repeated.

            Ex: n = 1
            [1, 1]

            Ex: n = 2
            [1, 2, 2]

            or 

            [1, 1, 2]

            Ex: n = 4

            [1, 2, 4, 4, 4] # we can repeat numerous times


            since we need O(1) space we cannot store seen except for last element seen. Thus we wouldn't be able to traverse linearly becasue the duplicate numbers may not be next to each other.

            How about using their values as pointers

            [1, 2, 4, 4, 4]
             ^
            [1, 2, 4, 4, 4]
                ^
            [1, 2, 4, 4, 4]
                    ^    
            [1, 2, 4, 4, 4]
                         ^
            ...
            so interesting that 4 was hit twice 
            This creates a cycle

            Try another example
            n = 4
            [1,2,3,2,2]
             ^
            [1,2,3,2,2]
               ^
            [1,2,3,2,2]
                 ^
            [1,2,3,2,2]
                   ^
            [1,2,3,2,2]
                 ^
            ... Creates a cycle

            What I know from linked lists and cycles is we can use fast and slow pointers to identify a cycle, will converge at some point in the cycle. But identifying where can help us see where the duplicate character is

            [1,2,3,2,2]
            Slow and fast pointers here converge at 3
            slow.next = duplicate

            [1, 2, 4, 4, 4]
            
            slow and fast pointers converge at 4
            slow and slow.next = duplicate 

            [1, 2, 3, 4, 5, 3]
                      sf

            converge at 4  

            the duplicates have to be a part of the cycle

        '''
        # if len(nums) == 2:
        #     return nums[0]

        # slow = 0
        # fast = 0

        # slow = nums[slow]
        # fast = nums[nums[fast]]
        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]

        # slow2 = 0

        # while slow2 != slow:
        #     slow = nums[slow]
        #     slow2 = nums[slow2]
        
        # return slow2


        # Modifying the original array solution

        for num in nums:
            idx = abs(num) # No -1 needed!
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1
        return -1




            
