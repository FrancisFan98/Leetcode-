# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        rs = ListNode(None)
        cur = rs
        while head != None:
            if head.val != val:
                cur.next = ListNode(head.val)
                cur = cur.next
            head = head.next
            
        
            
        return rs.next
        
        
