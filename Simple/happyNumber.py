class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def ans(n):
            rs = 0
            while n > 0:
                rs += (n % 10) ** 2
                n /= 10
            return rs
        
        record = set()
        while True:
            if n in record:
                return False
            
            if sum([int(i) for i in str(n)]) == 1:
                print (record)
                return True
            
            record.add(n)
            n = ans(n)
