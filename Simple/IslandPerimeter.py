class Solution(object):
    def countPerimeter(self, row, col, grid):
        upper = grid[row-1][col] if row - 1 >= 0 else 0
        lower = grid[row + 1][col] if row + 1 < len(grid) else 0
        left = grid[row][col - 1] if col - 1 >= 0 else 0        
        right = grid[row][col + 1] if col + 1 < len(grid[row]) else 0
        surround = [upper, lower, left, right]
        best = 4
        
        for pos in surround:
            if pos == 1:
                best -= 1
        
        return best
        
        
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rs = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == 1:
                    rs += self.countPerimeter(i, j, grid)
        return rs
