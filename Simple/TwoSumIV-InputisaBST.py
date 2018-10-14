# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        queue = [root]
        record = set()
        while queue:
            
            node = queue.pop()
            if not node:
                continue

            need = k - node.val
            if need in record:
                return True
            
            record.add(node.val)
            queue.extend([node.left, node.right])
        return False
            
        """        def find(root, v):
            if not root :
                return False
            if root.right and root.right.val == v:
                return True
            if root.left and v == root.left.val:
                return True
            elif v > root.val:
                return find(root.right, v)
            else:
                return find(root.left, v)
        
        queue = [root]
        while queue:
            node = queue.pop()
            if not node:
                continue
            need = k - node.val
            
            if node.val == need:
                f = (node.left and node.left.val == need) or (node.right and node.right.val == need)
                if f:
                    return True   
                else:
                    queue.extend([node.left, node.right])
                    continue
            
            if find(root, need):
                return True
            else:
                queue.extend([node.left, node.right])
        return False
        """
