class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(N) space with O(N) time complextity

        # seen = set()

        # for n in nums:
        #     if n in seen:
        #         return n
        #     else:
        #         seen.add(n)
        

        # O(1) space complexity: Need to use pointers


        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1
        return -1
            
        
        
        