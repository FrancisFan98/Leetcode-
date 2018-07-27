# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        rt = [root]
        maxn = 0
        while rt != []:
            old, new = rt, []
            for item in old:
                new.append(item.left)
                new.append(item.right)
            rt = [node for node in new if node ]
            maxn += 1
        return maxn
