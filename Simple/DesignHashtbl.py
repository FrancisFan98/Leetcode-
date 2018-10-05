class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 8096
        self.map = [None] * 8096
        

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        hashkey = key % self.size
        
        if self.map[hashkey] == None:
            self.map[hashkey] = [key]
        else:
            if key not in self.map[hashkey]:
                self.map[hashkey].append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        hashkey = key % self.size
        if self.map[hashkey] == None:
            return 
        
        for i in range(len(self.map[hashkey])):
            if self.map[hashkey][i] == key:
                self.map[hashkey].pop(i)
                return 
            
        return 

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hashkey = key % self.size
        if self.map[hashkey] == None:
            return False
        
        for i in range(len(self.map[hashkey])):
            if self.map[hashkey][i] == key:
                return True
        return False
        
        


