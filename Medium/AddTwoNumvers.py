# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        
        expo = 0
        rs = []
        while l1 and l2:
            rs.append((l1.val + l2.val) * 10 ** expo)
            l1 = l1.next
            l2 = l2.next
            expo += 1
        while l1:
            rs.append(l1.val * 10 ** expo)
            expo += 1
            l1 = l1.next
        while l2:
            rs.append(l2.val * 10 ** expo)
            expo += 1
            l2 = l2.next
        rs = sum(rs)
        if rs < 10 ** expo:
            expo -= 1
        
        new = None
        
        while expo >= 0:
            newnode = ListNode(rs // 10 ** expo)
            newnode.next = new
            new = newnode
            rs = rs % 10 ** expo
            expo -= 1
            
         
                 
        return new
            
