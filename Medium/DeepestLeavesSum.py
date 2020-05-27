# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def deepestLeavesSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    
    # def find_level(root, level):
    #     if not root:
    #         return -1
    #     if not root.left and not root.right:
    #         return level
        
    #     return max(find_level(root.left, level + 1), find_level(root.right, level + 1))
    
    # max_depth = find_level(root, 0)

    
    # def count_deepest(root, level, rs):
    #     # print(max_depth)

    #     if not root:
    #         return rs
    #     if level == max_depth:
    #         rs += root.val
    #     else:
    #         rs = count_deepest(root.left, level + 1, rs)
    #         rs = count_deepest(root.right, level + 1, rs)
    #     return rs
    # rs = count_deepest(root, 0, 0)
    # return rs
            


def deepestLeavesSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    
    q = [root]
    while q:
        next_level = []
        for i in range(len(q)):
            node = q[i]
            if node.right:
                next_level.append(node.right)
            if node.left:
                next_level.append(node.left)
                
        if next_level:
            q = next_level
        else:
            break
    
    rs = sum([node.val for node in q])
    return rs
    

