class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        
        
        
        n,m = len(M), len(M[0])
        if n == m ==1:
            return M
        
        rs = []
        for i in range(n):
            rs.append([i for i in range(m)])
        rs[0][0] = 5
        
        if n == 1:
            for i in range(1,m-1):
                rs[0][i] = (M[0][i-1] + M[0][i] + M[0][i+1])//3
            rs[0][0] = (M[0][0] + M[0][1])//2
            rs[0][-1] = (M[0][-2] + M[0][-1])//2

            return rs

        if m == 1:
            for i in range(1,n-1):
                rs[i][0] = (M[i][0] + M[i-1][0] + M[i+1][0])//3
            rs[0][0] = (M[0][0] + M[1][0])//2
            rs[-1][0] = (M[-1][0] + M[-2][0])//2
            return rs
        
        
        
        for i in range(1, n-1):
            for j in range(1, m-1):
                rs[i][j] = (M[i-1][j-1] + M[i-1][j] + M[i-1][j+1] + M[i][j-1] + M[i][j] + M[i][j+1] + M[i+1][j-1] + M[i+1][j] + M[i+1][j+1]) // 9
        print (rs)
        
        rs[0][0] = (M[0][0] + M[0][1] + M[1][0] + M[1][1]) // 4
        rs[0][m-1] = (M[0][m-2] + M[0][m-1] + M[1][m-2] + M[1][m-1]) // 4   
        rs[n-1][0] = (M[n-1][0] + M[n-1][1] + M[n-2][0] + M[n-2][1]) // 4
        rs[n-1][m-1] = (M[n-1][m-2] + M[n-1][m-1] + M[n-2][m-2] + M[n-2][m-1]) // 4  
        
        
        for j in range(1, m-1):
            rs[0][j] = (M[0][j-1] + M[0][j] + M[0][j+1] + M[1][j-1]  + M[1][j]  + M[1][j+1]) // 6
        for j in range(1, m-1):
            rs[n-1][j] = (M[n-1][j-1] + M[n-1][j] + M[n-1][j+1] + M[n-2][j-1]  + M[n-2][j]  + M[n-2][j+1]) // 6
            
        for i in range(1, n-1):
            rs[i][0] = (M[i][0] + M[i][1] + M[i-1][0] + M[i-1][1]  + M[i+1][0]  + M[i+1][1]) // 6
        for i in range(1, n-1):
            rs[i][m-1] = (M[i-1][m-1] + M[i-1][m-2] + M[i][m-1] + M[i][m-2]  + M[i+1][m-1]  + M[i+1][m-2]) // 6
            
        
        return rs
