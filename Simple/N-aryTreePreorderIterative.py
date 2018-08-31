"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        rs = []
        if not root:
            return rs
        
        queue = [root]
        while queue:
            node = queue.pop()
            for child in node.children[::-1]:
                queue.append(child)
            rs.append(node.val)
        
        return rs
