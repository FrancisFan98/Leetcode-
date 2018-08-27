class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        
        m = int(math.sqrt(area))
        
        while m > 0:
            if area % m == 0:
                return [area/m, m] 
            else:
                m -= 1
        return 0
