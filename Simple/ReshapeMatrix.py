class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        flat = sum(nums, [])
        if len(flat) != r*c:
            return nums
        
        return [flat[x:x+c] for x in range(0,len(flat), c)]
        
