# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        def getLength(root):
            length = 0
            while root != None:
                length += 1
                root = root.next
            return length
        
        lengthA = getLength(headA)
        lengthB = getLength(headB)
        

        
        longer = headA if lengthA > lengthB else headB
        shorter = headA if lengthA <= lengthB else headB
        
        for i in range(abs(lengthA - lengthB)):
            longer = longer.next
        
        while longer != None:
            if longer == shorter:
                return longer
            longer = longer.next
            shorter = shorter.next
            
        
        return None
