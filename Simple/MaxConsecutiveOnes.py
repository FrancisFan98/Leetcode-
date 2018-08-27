class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        rs = []
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                rs.append(count)
                count = 0
        if count:
            rs.append(count)
        
        return max( rs ) if rs else 0
