# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        
        count = 0
        cur = head
        while cur != None:
            count += 1
            cur = cur.next
        if count < 2:
            return True
        
        prev = None
        cur = head
        for i in range(count // 2):
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
            
        if count % 2:
            cur = cur.next
            
        while cur != None and prev != None:
            if cur.val != prev.val:
                return False
            
            cur = cur.next
            prev = prev.next
            
        return True
