
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        def nodePath(root, node):
            path = []
            while root != None:
                if node.val > root.val:
                    path.insert(0, root)
                    root = root.right
                elif node.val < root.val:
                    path.insert(0, root)
                    root = root.left
                else:
                    path.insert(0, root)
                    return path
            return path
        
        ppath = nodePath(root, p)
        qpath = nodePath(root, q)
        
        
        for node in ppath:
            for node2 in qpath:
                print (node.val, node2.val)
                if node.val == node2.val:
                    return node
        return None"""
        
        small, large = min(q.val, p.val), max(q.val, p.val)
        if small <= root.val <= large:
            return root
        
        if root.val > large:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right,p, q)
        
    
