class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p, r = 0, len(nums)-1
        
        while r >= p:
            
            
            if nums[p] == val:
                nums[p] = nums[r]
                r -= 1
            if nums[p] != val:
                p += 1
        return r+1
        
