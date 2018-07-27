# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        rs = []
        rl = [root]
        
        while rl != []:
            
            rs.append([node.val for node in rl])
            
            level = []
            for item in rl:
                if item.left:
                    level.append(item.left)
                if item.right:
                    level.append(item.right)
            
            rl = [node for node in level if node]
            
        return list(reversed(rs))
