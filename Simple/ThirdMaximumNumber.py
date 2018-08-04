class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       

        first, second, third = -sys.maxint, -sys.maxint, -sys.maxint
        
        for i in nums:
            if i > first:
                second, third = first, second
                first = i
            elif second < i < first:
                third = second
                second = i
            elif third < i < second:
                third = i
        return third if third != -sys.maxint else first
