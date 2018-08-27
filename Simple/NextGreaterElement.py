class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        
        if not findNums:
            return []
        rs = []
        for x in findNums:
            index = nums.index(x)
            flag = True
            for j in range(index+1, len(nums)):
                if nums[j] > x:
                    rs.append(nums[j])
                    flag = False
                    break
            print (flag)
            if flag:
                rs.append(-1)
            
        return rs"""
        
        stack = []
        rs ={}
        
        for num in nums:
            while stack and stack[-1] < num:
                rs[stack.pop()] = num
            stack.append(num)
            
        return [ rs[x] if x in rs else -1 for x in findNums ]
