class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        
        # Starting both at 0
        max_height_l = 0
        max_height_r = 0
        
        volume = 0

        while l < r:
            # 1. Capture current wall heights into max tracking FIRST
            max_height_l = max(max_height_l, height[l])
            max_height_r = max(max_height_r, height[r])

            # 2. Add water and THEN step pointer
            if max_height_l < max_height_r:
                volume += max_height_l - height[l]
                l += 1
            else:
                volume += max_height_r - height[r]
                r -= 1

        return volume




        # volume = 0

        
        # l = 0
        # r = len(height) - 1

        # max_height_l = height[l]
        # max_height_r = height[r]
        # while l < r:
        #     if max_height_l < max_height_r:
        #         l += 1
        #         max_height_l = max(height[l], max_height_l)
        #         volume += max_height_l - height[l]
        #     else:
        #         r -= 1
        #         max_height_r = max(height[r], max_height_r)
        #         volume += max_height_r - height[r]

        # return volume