class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            # if out of bounds or water, stop
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            # mark as visited
            grid[r][c] = "0"
            # visit all 4 directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1  # found a new island
                    dfs(r, c)
        
        return count
