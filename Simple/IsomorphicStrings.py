class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        record = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):

            if s[i] not in record:
                record[s[i]] = t[i]
            
            if record[s[i]] != t[i]:
                return False
            
            if record.values().count(t[i]) > 1:
                return False
        
        return True
