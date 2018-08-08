class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        times = minutesToTest // minutesToDie
        
        for pig in range(1, buckets):
            if (times + 1) ** pig >= buckets:
                return pig
            
        return 0
        
