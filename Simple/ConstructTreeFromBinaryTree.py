#definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t or t.val == None :
            return ''
        if not t.left and not t.right:
            return str(t.val)
         
        
        rs = str(t.val) + "(" + self.tree2str(t.left) + ")" + "(" + self.tree2str(t.right) + ")"
        if rs[-2:] == "()":
            return rs[:-2]
        return rs
        
