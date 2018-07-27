class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        
        
        pivot = len(nums) - k 
        nums[pivot:] = list(reversed(nums[pivot:]))
        nums[:pivot] = list(reversed(nums[:pivot]))
        nums[:] = list(reversed(nums))
        
