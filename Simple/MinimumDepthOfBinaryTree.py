# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        rl = [root]
        depth = 0
        
        while rl:
            depth += 1
            old, new = rl, []
            
            for item in old:
                if item.left == item.right == None:
                    return depth
                new.append(item.left)
                new.append(item.right)
            new = [node for node in new if node != None]
            rl = new
            
        
        return "NO WAY"
