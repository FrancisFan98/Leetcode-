class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        if num < 2:
            return True
        
        left = 0
        right = num // 2
        
        while right >= left:
            
            mid = left + (right - left) // 2
            if mid ** 2 == num:
                return True
            if mid ** 2 < num:
                left = mid + 1
            else:
                right = mid - 1
                
        return mid ** 2 == num
            
