Class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
       
        maxv = sum(nums[:k])
        temp = maxv
        
        for i in range(k, len(nums)):
            temp = temp - nums[i-k] + nums[i]
            if temp > maxv:
                maxv = temp
        return maxv / float(k)
