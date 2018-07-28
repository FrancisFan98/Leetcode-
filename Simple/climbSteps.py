class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        first = 0
        second = 1
        
        for i in range(n):
            first, second = second, second + first
        
        return second
        
