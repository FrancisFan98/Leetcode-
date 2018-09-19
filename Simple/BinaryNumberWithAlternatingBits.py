class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 0:
            if not ((n % 4) == 1 or (n % 4) == 2):
                return False
            n = n >> 1
        return True
            
