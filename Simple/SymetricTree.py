# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        queue = [root]
        
        while queue:
            old, new = queue, []
            for item in old:
                if item.left == None:
                    new.append('null')
                else:
                    new.append(item.left)
                if item.right == None:
                    new.append("null")
                else:
                    new.append(item.right)
            
            queue = [node for node in new if node != "null"]
            
                
            if [node.val if node != "null" else "null" for node in new] != [node.val if node != "null" else "null" for node in new[::-1]]:
                return False
        
        return True
