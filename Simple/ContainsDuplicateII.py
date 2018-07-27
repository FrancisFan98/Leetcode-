class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        record = {}
        
        if not nums:
            return False
        
        for i in range(len(nums)):
            if nums[i] in record and i - record[nums[i]] <= k:
                return True

            
            record[nums[i]] = i
        return False
