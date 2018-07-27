class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        exponent = 0
        negFlag = x < 0
        x = abs(x)
        rs = x%10
        x = x//10
        while x > 0:
            rs *=10
            rs += x%10
            x = x//10
        
        if rs > 2**31:
            return 0
        return -rs if negFlag else rs 
        
