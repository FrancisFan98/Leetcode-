class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        
        Max = max(nums)
        n = len(nums)
        rs = 0
        
        while sum(nums) != n*Max:
            index = nums.index(Max)
            nums[index] -= 1
            Max = max(nums)
            rs += 1
        
        return rs"""
        
        return sum(nums) - len(nums) * min(nums)
        
