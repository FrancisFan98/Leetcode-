# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        left, right = 1, n
        mid = left + (right - left) // 2
        while guess(mid) != 0:
            if guess(mid) == 1:
                left = mid + 1
            else:
                right = mid - 1
            mid = left + (right - left) // 2
        return mid
