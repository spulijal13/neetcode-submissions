class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        m = len(grid)
        n = len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == '0'):
                return
            
            grid[r][c] = '0'
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands