class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.size:
            return -1
        else:
            cur = self.head
            while index > 0:
                index -= 1
                cur = cur.next
            return cur.val
        
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        if self.head == None:
            self.head = Node(val)
            self.size += 1
        else:
            new = Node(val)
            new.next = self.head
            self.head = new
            self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if self.head == None:
            self.head = Node(val)
            self.size += 1
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(val)
            self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index > self.size:
            return
        elif index == self.size:
            self.addAtTail(val)
        else:
            cur = self.head
            while index-1 > 0:
                cur = cur.next
                index -= 1
            nex = cur.next
            cur.next = Node(val)
            cur.next.next = nex
            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index >= self.size:
            return
        else:
            cur = self.head
            prev = None
            while index > 0:
                index -= 1
                prev = cur
                cur = cur.next
            prev.next = cur.next
            self.size -= 1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
