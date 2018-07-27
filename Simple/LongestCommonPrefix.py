class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        temp = strs[0]
        strs = list(zip(strs))
        
        rs = 0
        for i in range(len(strs)):
            simp = set(strs[i])
            if len(simp) == 1:
                rs += 1
                continue
            break
        return temp[:rs + 1]
