class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        rs = {}
        for i in range(len(list1)):
            rs[list1[i]] = i + 10000
        
        for i in range(len(list2)):
            if list2[i] in rs:
                rs[list2[i]] += i - 10000
        
        minv = min(rs.values())
        ans = []
        for k, v in rs.items():
            if v == minv:
                ans.append(k)
                
        return ans
            
        
