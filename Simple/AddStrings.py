class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        longer = num1 if len(num1) >= len(num2) else num2
        shorter = num1 if len(num2) > len(num1) else num2
        
        
        while len(shorter) != len(longer):
            shorter = "0" + shorter
        
        longer = [ord(x) for x in longer]
        shorter = [ord(x) for x in shorter]
        
        rs = []
        carry = 0
        for i in range(1, len(longer) + 1):
            if shorter[-i] + longer[-i] - 48 + carry > 57:
                rs.insert(0, shorter[-i] + longer[-i] - 48 + carry - 10)
                carry = 1
            elif shorter[-i] + longer[-i] - 48 + carry < 48:
                rs.insert(0, shorter[-i] + longer[-i] - 48 + carry + 10)
                carry = -1
            else:
                rs.insert(0, shorter[-i] + longer[-i] - 48 + carry)
                carry = 0
                
        if carry:
            rs.insert(0, 49)
        
        return "".join([chr(x) for x in rs])
