class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        if len(flowerbed) <= 2:
            return n <= 1 if sum(flowerbed) == 0 else n == 0
        
        
        index = 1
        count = 0
        if flowerbed[0] == flowerbed[1] == 0:
            count += 1
            flowerbed[0] = 1
            
        while index < len(flowerbed)-1:
            if flowerbed[index-1] == flowerbed[index] == flowerbed[index+1] == 0:
                count += 1
                
                flowerbed[index] = 1
            
            index += 1
            
        if flowerbed[-1] == flowerbed[-2] == 0:
            
            count += 1
        return count >= n
