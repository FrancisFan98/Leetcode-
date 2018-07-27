class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        q = len(s) - 1
        rs = [0 for i in range(len(s))]
        
        for i in range(len(s)):

            rs[i] = s[i]
            
            if s[i] in vowels:
                while s[q] not in vowels:
                    q -= 1
                rs[i] = s[q]
                q -= 1 
        return "".join(rs)

