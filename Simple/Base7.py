class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        rs = []
        
        num1 = abs(num)
        
        while num1 > 0:
            rs.insert(0, str(num1%7))
            num1 = num1 / 7
            
        return "".join(rs) if num >= 0 else "-" + "".join(rs)
