# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        
        if root == None:
            return root
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right,left
        
        return root"""
        
        
        if root == None: 
            return None
        q = [root]
        while q:
            node = q.pop(0)
            node.left, node.right = node.right, node.left
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return root
