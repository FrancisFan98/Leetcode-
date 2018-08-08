class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        rs = 0
        g = list(sorted(g))
        s = list(sorted(s))
        
        cIndex = 0
        kIndex = 0
        
        while cIndex < len(s) and kIndex < len(g):
            if s[cIndex] >= g[kIndex]:
                rs += 1
                cIndex += 1
                kIndex += 1
                
            else:
                cIndex += 1
        return rs
        
