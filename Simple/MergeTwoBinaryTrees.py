# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        head = None
        if t1 and t2:
            head = TreeNode(t1.val + t2.val)
            head.left = self.mergeTrees(t1.left, t2.left)
            head.right = self.mergeTrees(t1.right, t2.right)
        elif t1:
            return t1
        elif t2:
            return t2
        
        return head
        
        
        
