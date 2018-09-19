class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if not set(B).issubset(A):
            return -1
        
        k, r = divmod(len(B), len(A))
        if r > 0:
            k += 1
        temp = k * A
        if B not in temp:
            k += 1
            temp += A
        else:
            return k
        if B in temp:
            return k

        return -1
