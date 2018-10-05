class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 8096
        self.map = [None] * self.size
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        hashkey = sum([ord(x) for x in str(key)]) % self.size
        
        if self.map[hashkey] == None:
            self.map[hashkey] = [[key, value]]
            return
        else:
            for pair in self.map[hashkey]:
                if pair[0] == key:
                    pair[1] = value
                    return
            self.map[hashkey].append([key, value])
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashkey = sum([ord(x) for x in str(key)]) % self.size
        
        if self.map[hashkey] == None:
            return -1
        
        for pair in self.map[hashkey]:
            if pair[0] == key:
                return pair[1]
        return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        hashkey = sum([ord(x) for x in str(key)]) % self.size
        
        if self.map[hashkey] == None:
            return 
        
        for i in range(len(self.map[hashkey])):
            if self.map[hashkey][i][0] == key:
                self.map[hashkey].pop(i)
                return
        return
                
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
