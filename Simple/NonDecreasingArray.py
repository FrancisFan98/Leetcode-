class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        index = None
        for i in range(len(nums) -1):
            if nums[i] > nums[i+1]:
                if index != None:
                    return False
                else:
                    index = i
        
        return (index == None or index == 0 or index == len(nums) - 2 or nums[index-1] <= nums[index + 1] or nums[index] <= nums[index+2]  )
        
