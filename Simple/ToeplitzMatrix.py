class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all([c == 0 or r == 0 or matrix[r-1][c-1] == matrix[r][c] for r in range(len(matrix)) for c in range(len(matrix[r]))])
        
