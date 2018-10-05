class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        record = {}
        first = {}
        last = {}
        
        for i in range(len(nums)):
            if nums[i] not in record:
                record[nums[i]] = 1
                first[nums[i]] = i
                last[nums[i]] = i
            else:
                record[nums[i]] += 1
                last[nums[i]] = i
                
        
        rs = [x for x in record if record[x] == max(record.values())]
        
        return min([last[x] - first[x] + 1 for x in rs])
