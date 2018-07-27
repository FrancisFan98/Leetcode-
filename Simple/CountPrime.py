class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        
        rs = [True] * n
        rs[0] = rs[1] = False
        for i in range(2, (n+1)/2):
            rs[i*i : n: i] = [False] * len(rs[i*i : n :i])
        return sum(rs)
            
        
