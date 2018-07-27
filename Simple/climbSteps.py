class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        rs = 0
        first = 0
        second = 1
        
        for i in range(n):
            first, second = second, second + first
        
        return second
        
