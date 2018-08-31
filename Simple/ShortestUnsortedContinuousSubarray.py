class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        B = sorted(nums)
        first = 0
        second = 0
        if nums == B:return 0
        for i in xrange(len(nums)):
            if B[i] != nums[i]:
                first = i
                break
        
        for j in xrange(len(nums)-1, -1,-1):
            if B[j] != nums[j]:
                second = j
                break
        
        return second - first + 1
