class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        q, r = 0, x
        mid = x // 2
        
        if x == 1:
            return 1
        if x == 0:
            return 0
        
        while r > q :
            if mid ** 2 <= x and (mid + 1) ** 2 > x:
                return mid
            else:
                if x < mid ** 2:
                    r = mid 
                    mid = (r + q) // 2
                else:
                    p = mid 
                    mid = (r + p) // 2
        return False
