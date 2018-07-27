# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return []
        
        cur = head
        val = cur.val
        while cur.next != None:
            next1 = cur.next
            if next1.val == val:
                cur.next = next1.next
            else:
                cur = next1
                val = cur.val
        return head
