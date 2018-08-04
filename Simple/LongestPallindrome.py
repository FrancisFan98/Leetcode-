class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = {}
        for cha in s:
            if cha in record:
                record[cha] += 1
            else:
                record[cha] = 1
        
        rs = 0
        oddflag = 0
        for v in record.values():
            if v % 2 == 0:
                rs += v
            else:
                rs += v - 1
                oddflag = 1
        
        if oddflag:
            rs += 1

        return rs 
