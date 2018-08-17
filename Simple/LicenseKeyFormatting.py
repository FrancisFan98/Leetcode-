class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
	Learned that string comparison is extremely slow
        """        
        
        S = "".join(S.split("-"))        
        first = K if len(S) % K == 0 else len(S) % K
        
        rs = [S[:first] ]
        count = 0
        S = S[first:]
        
        for i in range(0,len(S),K):
            rs.append(S[i:i+K])
            
        return "-".join(rs).upper()
