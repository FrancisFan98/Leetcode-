class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        rs = {}
        for cha in t:
            if cha not in rs:
                rs[cha] = 1
            else:
                rs[cha] += 1
                
        for cha in s:
            rs[cha] -= 1
        
        for k, v in rs.items():
            if v == 1:
                return k
        return None
