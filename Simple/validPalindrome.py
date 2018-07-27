import string
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        
        p, r = 0, len(s) - 1
        while r >= p:
            if s[p] not in string.ascii_letters + string.digits:
                p += 1
                continue
            if s[r] not in string.ascii_letters + string.digits:
                r -= 1 
                continue
            if s[p] != s[r]:
                return False
            p += 1
            r -= 1
        return True
