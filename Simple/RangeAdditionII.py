class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return n*m
        minx = min([x[0] for x in ops])
        miny = min([y[1] for y in ops])
        
        return minx*miny
        
        
        
