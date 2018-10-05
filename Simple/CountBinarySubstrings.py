class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        groups = [1]
        rs = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                groups[-1] += 1
            else:
                groups.append(1)
        
        for i in range(len(groups) -1):
            rs += min(groups[i], groups[i+1])
        
        return rs
        
