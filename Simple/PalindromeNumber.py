class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        q, r = 0, len(x) - 1
        
        while r > q:
            if x[r] != x[q]:
                return False
            q += 1
            r -= 1
        return True
