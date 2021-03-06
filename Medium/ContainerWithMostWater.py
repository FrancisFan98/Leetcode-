class Solution:
    def maxArea(self, height: List[int]) -> int:
        rs = 0
        l, r = 0, len(height)-1
        while r > l:
            rs = max(rs, (r-l)*min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return rs