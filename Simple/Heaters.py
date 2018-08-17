class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        rs = 0
        index = 0
        heaters =  sorted(heaters)
        houses = sorted(houses)
        
        for house in houses:
            while index < len(heaters) and house > heaters[index]:
                index += 1
                
            if index == 0:
                rs = max(rs, heaters[index] - house)
            elif index == len(heaters):
                rs = max(rs, house - heaters[-1])
            else:
                rs = max(rs, min(house - heaters[index-1], heaters[index] - house))
            
        
        
        
        return rs
