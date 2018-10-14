class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        cur = 0

        for i in range(len(A)):
            if not A[i] % 2:
                A[i], A[cur] = A[cur], A[i]
                cur += 1
        return A
