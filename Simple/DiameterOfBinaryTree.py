#definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    maxx = 0
    def recur(self,root):
        if not root:
            return 0
        L = self.recur(root.left)
        R = self.recur(root.right)
        
        self.maxx = max(L+R+1, self.maxx)
        return max(R,L) + 1
        
    
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.recur(root)
        return self.maxx -1
