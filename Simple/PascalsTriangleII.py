class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rs = [1]
        for i in range(rowIndex):
            rs = [j+k for j, k in zip([0] + rs, rs + [0])]
        return rs
