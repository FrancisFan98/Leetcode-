class Solution(object):
    def getSum(self, a, b):
	Max = 0x7FFFFFFF
	Min = 0x80000000
	mask = 0xFFFFFFFF

	while b != 0:
	    a, b = (a ^ b) & mask, (a & b) & mask
	return a if a <= Max else ~(a ^ mask)
