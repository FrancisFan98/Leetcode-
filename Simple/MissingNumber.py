class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        
        total = 0
        for i in range(len(nums) + 1 ):
            total += i
            
        
        for i in nums:
            total -= i
            
        return abs(total)
