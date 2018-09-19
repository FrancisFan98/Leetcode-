<<<<<<< HEAD
#definition for a binary tree node.
=======
# Definition for a binary tree node.
>>>>>>> 712dc8c2c09fa01ac59e6c62c87c11ec875d23db
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
<<<<<<< HEAD
=======
    
>>>>>>> 712dc8c2c09fa01ac59e6c62c87c11ec875d23db
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
<<<<<<< HEAD
        if not t1 and not t2:
            return None
        elif t1 and not t2:
            return t1
        elif t2 and not t1:
            return t2
        h = TreeNode(t1.val + t2.val)
        h.left = self.mergeTrees(t1.left, t2.left)
        h.right = self.mergeTrees(t1.right, t2.right)
        
        return h
=======
        
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
        
        
>>>>>>> 712dc8c2c09fa01ac59e6c62c87c11ec875d23db
        
