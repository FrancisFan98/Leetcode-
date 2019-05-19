class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:

        def eraseIsland(grid, i, j) -> None:
            adjacent = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for row, col in adjacent:
                if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                    continue
                else:
                    if grid[row][col] == "1":
                        grid[row][col] = "0"
                        eraseIsland(grid, row, col)
                    else:
                        continue

        rs = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "0":
                    continue
                elif grid[row][col] == "1":
                    rs += 1
                    eraseIsland(grid, row, col)
                else:
                    print ("wrong input")
        return rs
