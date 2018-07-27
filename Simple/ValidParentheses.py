class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
  
        sample = {"(" : ")", "[" : "]", "{" : "}"}
        
        left = []
        for i in range(len(s)):
            if s[i] in sample:
                left.append(i)
        
        for i in left[::-1]:
            if i + 1 > len(s) - 1:
                return False
            if sample[s[i]] == s[i+1]:
                s = s[:i] + s[i+2:]
                continue
            return False
        
        return not s
        
        
        
        
        
