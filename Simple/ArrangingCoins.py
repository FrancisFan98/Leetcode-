class Solution(object):
    import math
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        
        level = 1
        layers = 0
        while n - level >= 0:
            n -= level
            level += 1
            layers += 1
        return layers """
        
        return int((math.sqrt(1+8*n) - 1) // 2)
        
