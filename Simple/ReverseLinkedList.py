# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        if head == None:
            return []
        
        rs = None
        while head != None:
            new = ListNode(head.val)
            new.next = rs
            rs = new
            head = head.next
        return rs"""
        
        if head == None or head.next == None:
             return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return p
