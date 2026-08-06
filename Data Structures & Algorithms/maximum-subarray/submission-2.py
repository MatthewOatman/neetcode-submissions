class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        max_sum, curr = nums[0], 0

        for n in nums:
            curr += n
            max_sum = max(curr, max_sum)

            if curr < 0:
                curr = 0
            
        return max_sum