tion for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self, root):
        if not root:
            return 
        
        self.inorder(root.left)
        self.diff = min(self.diff, root.val - self.prev)
        self.prev = root.val
        self.inorder(root.right)
        
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = -999999999
        self.diff = 9999999999999
        self.inorder(root)
        
            
        return self.diff
