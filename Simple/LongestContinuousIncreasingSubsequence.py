class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        
        rs = []
        length = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                length += 1
            else:
                rs.append(length)
                length = 1  
        rs.append(length)
        return max(rs) if rs else len(nums)
