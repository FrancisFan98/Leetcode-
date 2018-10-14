class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        rs = [x for x in str]
        
        for i in range(len(rs)):
            n = ord(rs[i])
            if 64 < n < 91:
                rs[i] = chr(n + 32)    
        return "".join(rs)
