# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rs = set()
        
        queue = [root]
        while queue:
            node = queue.pop()
            if not node:
                continue
            rs.add(node.val)
            queue.append(node.right)
            queue.append(node.left)
        
        min1, ans = min(rs), float("inf")
        for v in rs:
            if min1 < v < ans:
                ans = v
            
        
        return -1 if ans == float('inf') else ans
