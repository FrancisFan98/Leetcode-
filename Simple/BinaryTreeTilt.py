# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    total = 0
    def inorder(self, root):
        if not root:
            return 0 
        
        left = self.inorder(root.left)
        
        right = self.inorder(root.right)
        self.total += abs(left - right)
        
        return root.val + left + right
        
    
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return self.total
        left = self.inorder(root)
        return self.total
