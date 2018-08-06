"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        n = len(grid)
        if all([v for row in grid for v in row ]):
            return Node(True, True, None, None, None, None)
        if all([not v for row in grid for v in row ]):
            return Node(False, True, None, None, None, None)
        
        return Node(False, False, 
                            self.construct([row[:n // 2] for row in grid[:n // 2]]),
                            self.construct([row[n // 2:] for row in grid[:n // 2]]),
                            self.construct([row[:n // 2] for row in grid[n // 2:]]),
                            self.construct([row[n // 2:] for row in grid[n // 2:]])
                           )
        
