class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return None
  
        
        expo = 0
        digits = 1
        
        #finding how many digits the target number will have
        while n / (digits * 9.0 * (10 ** expo)) > 1:
            n = n - (9 * (10 ** expo)) * digits
            digits += 1
            expo += 1
        
        #finding the target number
        num = math.ceil(n / digits) + 10 ** expo 
        n = n % digits

        num = int(num)
        if n == 0:
            num -= 1
            return int(str(num)[-1])
        else:
            
            return int(str(num)[n - 1])
        
        
