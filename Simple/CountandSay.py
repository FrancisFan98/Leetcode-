class Solution:
    def countAndSay(self, n):
        s = '1'
        
        if n == 1:
            return s
        
        def count(s):
            rs = ""
            ncount = 0
            cur = s[0]

            
            for i in range(len(s)):
                if s[i] == cur:
                    ncount += 1
                else:
                    if ncount == 0:
                        ncount += 1
                    rs = rs + str(ncount) + cur
                    cur = s[i]
                    ncount = 1
            
            if ncount == 0:
                ncount += 1
                
            rs = rs + str(ncount) + cur
            return rs
        
        for _ in range(n - 1):
            s = count(s)
            
        return s
