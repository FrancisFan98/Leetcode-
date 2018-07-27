class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = set(nums[:])
        length = len(temp)
        temp = list(temp)
        temp = sorted(temp)
        for i in range(len(temp)):
            nums[i] = temp[i]
        
        return length
