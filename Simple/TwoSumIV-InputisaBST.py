# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    record = {}
    def traverse(self, root,k):
        if not root:
            return 
        
        self.record[k - root.val] = root.val
        self.traverse(root.left, k) 
        self.traverse(root.right, k)
        
        return 
        
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        self.traverse(root,k)
        for v in self.record.values():
            if v in self.record:
                return True
        return False
            
        
