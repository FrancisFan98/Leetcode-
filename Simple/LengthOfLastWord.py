import string
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(set(s)) == 1 and s[0] == " ") or s == "": 
            return 0 
        if " " not in s:
            return len(s)
        
        p, r = 0, 0
        
        for i in range(len(s)):
            if s[i] == " " and i + 1 < len(s) and s[i + 1] != " ":
                p, r = i + 1 , i + 1
            if s[i] != " ":
                r += 1
        print (r, p)
        return r - p
