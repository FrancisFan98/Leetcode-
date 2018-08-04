class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        
        rs = ""
        All = "0123456789abcdef"
        
        for i in range(8):
            digit = num % 16
            rs = All[digit] + rs
            num = num >> 4
        return rs.lstrip("0")
