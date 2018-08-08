class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        
        times = minutesToTest // minutesToDie
        
        for pig in range(1, buckets):
            if (times + 1) ** pig >= buckets:
                return pig
            
        return 0
        """
	times = minutesToTest // minutesToDie
        
        # (times + 1) ** pigs >= buckets
        return int(math.ceil(math.log(buckets, times+1)))
