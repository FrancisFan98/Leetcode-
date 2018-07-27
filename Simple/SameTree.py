# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not q and not p:
            return True
        if not q or not p:
            return False
        
        pList = [p.val]
        qList = [q.val]
        
        def search(node):
            left = node.left
            right = node.right
            rs = []
            
            if right == left == None:
                return []
            
            if left != None:
                rs.append(left.val)
                rs += search(left) 
            else:
                rs.append('null')
            if right != None:
                rs.append(right.val)
                rs += search(right)
            else:
                rs.append('null')
            return rs
        
        pList += search(p)
        qList += search(q)
        
        print (qList, pList)
        
        return pList == qList
        
        
            
