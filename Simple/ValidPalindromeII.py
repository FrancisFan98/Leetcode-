ass Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 2:
            return True
        
        sr = s[::-1]
        new = []
        for i in range(len(s)):
            if s[i] != sr[i]:
                new.extend([(s[:i] + s[i+1:]), (sr[:i] + sr[i+1:])])
                break
                
        if not new:
            return True
        isP = lambda x : x == x[::-1]
        return any([isP(x) for x in new]) 
        
