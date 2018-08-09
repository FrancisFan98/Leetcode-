class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        
        new = x^y
        rs = 0
        for cha in bin(new):
            if cha == "1":
                rs += 1
        return rs"""
        new = x ^ y
        rs = 0
        while new > 0:
            rs += new & 1
            new = new >> 1
        return rs
