class Solution(object):
    def isSelfDividing(self, n):
        temp = n
        while temp > 0:
            digit = temp % 10 
            if digit == 0 or n % digit:
                return False
            temp /= 10
        return True
        
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        rs = []
        
        for i in range(left, right+1):
            if self.isSelfDividing(i):
                rs.append(i)
        return rs
