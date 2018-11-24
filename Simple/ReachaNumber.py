import math

class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        t = abs(target)
        n = math.ceil((math.sqrt(8*t+1)-1)/2)
        d = n*(n+1)/2-t
        if d % 2 == 0:
            return n
        elif (d+n+1) % 2 == 0:
            return n+1
        else:
            return n+2

