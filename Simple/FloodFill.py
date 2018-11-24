class Solution(object):
    def find(self,image, sr, sc, color):
        rs = []
        if sr - 1 >= 0 and image[sr-1][sc] == color:
            rs.append((sr-1, sc))
        if sr + 1 < len(image) and image[sr+1][sc] == color:
            rs.append((sr+1, sc))
        if sc - 1 >= 0 and image[sr][sc-1] == color:
            rs.append((sr, sc-1))
        if sc + 1 < len(image[sr]) and image[sr][sc+1] == color:
            rs.append((sr, sc+1))
        return rs
        
        
        
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        visited = []
        new = [(sr, sc)]
        originColor = image[sr][sc]
        while new:
            node = new.pop()
            if node in visited:
                continue
            
            visited.append(node)
            new.extend(self.find(image, node[0], node[1], originColor))     
        
        for r, c in visited:
            image[r][c] = newColor
        
        
        return image
        
