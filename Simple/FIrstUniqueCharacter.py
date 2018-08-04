class Solution(object):
    import collections
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        rs = {}
        for cha in s:
            if cha not in rs:
                rs[cha] = 1
            else:
                rs[cha] += 1
                
        for i in range(len(s)):
            if rs[s[i]] == 1:
                return i
        return -1
