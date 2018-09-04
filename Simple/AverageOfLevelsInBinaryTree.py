#definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        rs = []
        queue = [root]
        while queue:
            children = []
            level = []
            while queue:
                node = queue.pop()
                if not node:
                    continue
                children.append(node.left)
                children.append(node.right)
                level.append(node.val)
            if not level:
                continue
            rs.append(sum(level) / float(len(level)))
            queue.extend(children)
        
        return rs
