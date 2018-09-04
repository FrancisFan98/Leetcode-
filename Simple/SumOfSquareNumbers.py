ass Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c == 0:
            return True
        for i in range(int(math.ceil(math.sqrt(c)))):
            b = math.sqrt(c - i**2)
            if b == int(b):
                return True
        return False
