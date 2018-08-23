ass Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        if k == 0:
            return len( [x for x in collections.Counter(nums).values() if x > 1  ] )
        else:
            return len(set([x+k for x in nums]) & set(nums))
        
        
            
        
