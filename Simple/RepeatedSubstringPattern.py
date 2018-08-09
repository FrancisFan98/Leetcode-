class Solution(object):
    
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = (s + s)[1:-1]
        return s in new
        """
        n = len(s)
        for i in range(1, len(s)):
            if n % i != 0:
                continue
            p = s[:i]
            if p * (n/len(p)) == s:
                return True
        return False"""
            
