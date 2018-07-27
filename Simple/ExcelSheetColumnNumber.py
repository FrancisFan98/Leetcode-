class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        rs = 0
        expo = 0
        letters = string.ascii_uppercase
        for char in s[::-1]:
            rs = rs + (letters.index(char) + 1) * ( 26 ** expo)
            expo += 1
        return rs
                      
            
