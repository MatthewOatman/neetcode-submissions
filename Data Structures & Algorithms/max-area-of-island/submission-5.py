class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        def dfs(r, c):
            # 1. Base Case: Check the CURRENT coordinates
            # If out of bounds or water, this path contributes 0 to the area
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            
            # 2. Mark as visited (Assignment, not equality!)
            grid[r][c] = 0
            
            # 3. Add the current cell (1) + the area of all 4 connected directions
            return (1 + 
                    dfs(r + 1, c) + 
                    dfs(r - 1, c) + 
                    dfs(r, c + 1) + 
                    dfs(r, c - 1))


        max_area = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    max_area = max(area, max_area)

        return max_area

