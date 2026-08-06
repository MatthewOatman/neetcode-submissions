class Solution:
    def trap(self, height: List[int]) -> int:
        
        volume = 0

        
        l = 0
        r = len(height) - 1

        max_height_l = height[l]
        max_height_r = height[r]
        while l < r:
            if max_height_l < max_height_r:
                l += 1
                max_height_l = max(height[l], max_height_l)
                volume += max_height_l - height[l]
            else:
                r -= 1
                max_height_r = max(height[r], max_height_r)
                volume += max_height_r - height[r]

        return volume