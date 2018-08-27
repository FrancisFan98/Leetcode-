"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        
        queue = [root]
        children = []
        depth = 0
        
        while queue:
            depth += 1
            while queue:
                node = queue.pop()
                for child in node.children:
                    if child != None:
                        children.append(child)
                
            
            queue = children
            children = []
        
        return depth
        
