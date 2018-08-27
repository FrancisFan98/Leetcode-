class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        flag = False
        prev = None
        prevp = None
        for cha in s:
            
            if cha == prev and cha == 'L' and cha == prevp:
                flag = True
                break
            prevp = prev
            prev = cha
                
        return s.count('A') <= 1 and not flag
