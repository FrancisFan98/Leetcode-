class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rs = []
        if numRows >= 1:
            rs.append([1])
        if numRows >= 2:
            rs.append([1, 1])
        
        if numRows > 2:
            for i in range(2, numRows):
                new = [1]
                last = rs[i - 1]
                for j in range(len(last) - 1):
                    new.append(last[j] + last[j+1])
                new.append(1)
                rs.append(new)
        return rs
