# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head
        if head == None or head.next == None:
            return False
        while cur != None :
            nex = cur.next    
            
            cur.next = cur
            if nex == None:
                return False
            if nex.next == cur:
                break
            cur = nex
        return True
