class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]
        rs = ""
        carry = 0
        la = len(a)
        lb = len(b)
        
        while (la > lb):
            lb += 1
            b += "0"
        while( lb > la):
            la += 1
            a += "0"
            
        
        for i in range(la):
            """if int(a[i]) + int(b[i]) + carry == 3:
                rs = "1" + rs
                carry = 1
            
            elif int(a[i]) + int(b[i]) + carry == 2:
                rs = "0" + rs
                carry = 1
                
            elif int(a[i]) + int(b[i]) + carry == 1:
                rs = "1" + rs
                carry = 0
                
            else:
                rs = "0" + rs
                carry = 0"""
            digit = int(a[i]) + int(b[i]) + carry
            mod = digit % 2
            if digit // 2 == 1:
                rs = str(mod) + rs
                carry = 1
            else:
                rs = str(mod) + rs
                carry = 0
            
        if carry:
            rs = "1" + rs
        return rs 
            
