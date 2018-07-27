class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = {}
        for num in nums:
            if num not in table:
                table[num] = 1
                continue
            table[num] += 1
        for key in table:
            if table[key] > len(nums)//2:
                return key
        return []
        
