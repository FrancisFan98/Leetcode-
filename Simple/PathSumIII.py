# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.numOfPath = 0
        self.dfs(root, sum)
        return self.numOfPath
    
    def dfs(self, root, sum):
        if root == None:
            return None
        
        self.test(root, sum)
        
        if root.left:
            self.dfs(root.left, sum)
        if root.right:
            self.dfs(root.right, sum)
    
    def test(self, root, sum):
        if root == None:
            return None
        
        if root.val == sum:
            self.numOfPath += 1
        
        if root.left:
            self.test(root.left, sum - root.val)
        if root.right:
            self.test(root.right, sum - root.val)
        
        
