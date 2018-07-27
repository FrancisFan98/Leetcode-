class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        rs = 0
        expo = 1
        while n // 5 > 0:
            rs = rs + n // 5 ** expo
            n = n // 5
        return rs
