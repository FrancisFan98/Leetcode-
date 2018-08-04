class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        rs = []
        for hour in range(12):
            for minute in range(60):
                if str(bin(hour)).count("1") + str(bin(minute)).count("1") == num:
                    rs.append("%i:%02i" % (hour, minute))
        return rs
            
