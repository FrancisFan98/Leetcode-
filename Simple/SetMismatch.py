ass Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = sum(set(nums))
        total = sum([i for i in range(len(nums)+1)])
        miss = total - a 
        more = sum(nums) - a
        return (more,miss)
