class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split(" ")
        s = [x for x in s if x != ""]
        return len(s)
        
        
