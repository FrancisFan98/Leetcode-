class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.data = [0]
        for i, v in enumerate(nums):
            self.data.append(self.data[i] + v)
        
            
                
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.data[j + 1] - self.data[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
