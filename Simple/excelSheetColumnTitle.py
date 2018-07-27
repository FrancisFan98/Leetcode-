class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        rs = []
        while n > 0:
            
            rs.append(string.ascii_uppercase[(n - 1) % 26 ])
            
            n = (n-1) / 26
            
        
        
        return "".join(list(reversed("".join(rs))))
