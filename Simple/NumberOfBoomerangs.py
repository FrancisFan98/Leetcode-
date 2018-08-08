class Solution(object):
    def countDistance(self, d1, d2):
        dx = abs(d1[0] - d2[0])
        dy = abs(d1[1] - d2[1])
        return math.sqrt(dx ** 2 + dy ** 2)
     
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        dist_dict = collections.defaultdict(int)
        rs = 0
        for i in range(len(points)):
            dist_dict.clear()
            for j in range(len(points)):
                if i == j:
                    continue
                distance = self.countDistance(points[i], points[j])
                dist_dict[distance] += 1
            for val in dist_dict.values():
                rs += val * (val-1)
        return rs
                
                
        
