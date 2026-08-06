class Solution:
    def canJump(self, nums: List[int]) -> bool:        
        # max reach approach

        # max_reach = 0

        # for i in range(len(nums)):

        #     # Then we are standing on a index that is unreachable and can't get to where we are standing
        #     if i > max_reach:
        #         return False
            
        #     #update max_reach
        #     max_reach = max(max_reach, i + nums[i])

        #     if max_reach >= len(nums) - 1:
        #         return True

    
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

            


            