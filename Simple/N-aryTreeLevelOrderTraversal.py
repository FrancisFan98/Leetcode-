"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        queue = [root]
        rs = []
        while queue:
            children = []
            layer = []
            
            for node in queue:
                layer.append(node.val)
                if node.children:
                    children += [child for child in node.children]
            rs.append(layer)
            
            queue = children
        return rs
