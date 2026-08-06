class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c):
            
            # return if we are out of bounds or to a cell that is 0
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
                return
            
            # this means that we have a 1:
            # set it to 0
            grid[r][c] = "0"

            # run dfs on the four directions
            dfs(r - 1, c) # top
            dfs(r, c + 1) # right
            dfs(r + 1, c) # down
            dfs(r, c - 1) # left


        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                # if we get to an land piece then we have an island and perfomr dfs 
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1

        return islands
        
                