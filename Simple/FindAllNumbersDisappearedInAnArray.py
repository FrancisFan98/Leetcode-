class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rs = []
        
        for index, val in enumerate(nums):
            i = abs(val) -1
            nums[i] = -abs(nums[i])
        for i in range(len(nums)):
            if nums[i] < 0:
                rs.append(index + 1)
        return rs
