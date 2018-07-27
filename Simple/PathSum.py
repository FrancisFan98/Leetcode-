# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def isGoalState(node):
            if node.left == node.right == None:
                return True
            return False
        
        rs = []
        total = 0
        def dfs(root, total = 0):
            if root == None:
                return 
            if isGoalState(root):
                rs.append(total + root.val)
            
            total += root.val
            a = dfs(root.left, total)
            b = dfs(root.right,total)

        dfs(root)
        return sum in (rs)
            
            
