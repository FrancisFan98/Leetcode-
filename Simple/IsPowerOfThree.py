class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and abs((math.log(n) / math.log(3)) - math.floor(math.log(n) / math.log(3) + 0.5)) <0.00000000001
