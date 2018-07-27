class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rs = 0
        for i in range(32):
            rs = (rs << 1) + (n & 1)
            n >>= 1
        return rs
    

