# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]

        return [str(root.val) + "{}{}".format('->', i) for i in self.binaryTreePaths(root.left)] + [str(root.val) + "{}{}".format("->", i) for i in self.binaryTreePaths(root.right)]
