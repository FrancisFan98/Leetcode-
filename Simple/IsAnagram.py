class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        records = {}
        recordt = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in records:
                records[s[i]] = 0
            else:
                records[s[i]] += 1
                
        for i in range(len(t)):
            if t[i] not in recordt:
                recordt[t[i]] = 0
            else:
                recordt[t[i]] +=1
                
        for key in records:
            if key not in recordt or records[key] != recordt[key]:
                return False
            
        return True
