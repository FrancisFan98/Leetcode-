ass Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        rs = num ^ 0xFFFFFFFF
        
        return int(bin(rs)[2:].lstrip('1'), 2)
