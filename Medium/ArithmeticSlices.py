class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3 : return 0
        new = []
        for i in range(len(A)-1):
            new.append(A[i+1] - A[i])
        
        cur = new[0]
        curn = 1
        rs = 0
        for i in range(1, len(new)):
            
            if cur == new[i]:
                curn += 1
                continue
            else:
                rs += curn * (curn-1) // 2
                curn = 1
                cur = new[i]
                
        rs += curn * (curn-1) // 2
        
        return rs
        
