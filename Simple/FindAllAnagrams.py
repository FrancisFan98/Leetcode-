ass Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or len(s) < len(p):
            return []
        dp = {}
        for cha in p:
            if cha in dp:
                dp[cha] += 1
            else:
                dp[cha] = 1
        
        lp = len(p)
        rs = []
        
        ds = {}
        for i in range(lp):
            if s[i] in ds:
                ds[s[i]] += 1
            else:
                ds[s[i]] = 1
        if ds == dp:
            rs.append(0)
        for i in range(lp, len(s)):
            ds[s[i-lp]] -= 1
            if ds[s[i-lp]] <= 0:
                del ds[s[i-lp]]
            if s[i] in ds:
                ds[s[i]] += 1
            else:
                ds[s[i]] = 1
            if ds == dp:
                rs.append(i-lp+1)
        return rs
