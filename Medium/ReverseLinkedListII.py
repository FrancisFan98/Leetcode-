# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        curr = self
        rs = []
        while curr:
            rs.append(str(curr.val))
            curr = curr.next
        return " ".join(rs)
        

def reverseBetween(head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    if m > n:
        return False
    
    reverse_len = n-m+1
    
    count = 1
    values = []
    curr = head
    while curr.next:
        if count == m:
            sub_curr = curr
            for _ in range(reverse_len):
                values.insert(0, sub_curr.val)
                sub_curr = sub_curr.next
            # print(values)
            sub_curr = curr
            for _ in range(reverse_len):
                sub_curr.val = values.pop(0)
                sub_curr = sub_curr.next
                
            return head
        count += 1
        curr = curr.next
    return False
                

                a,b,c,d,e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

print(reverseBetween(a, 2, 4))