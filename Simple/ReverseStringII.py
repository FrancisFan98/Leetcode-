ass Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        flag = 0
        rs = ''
        for i in range(0, len(s), k):
            if flag:
                flag = 0
                
                rs += s[i:i+k]
                continue
            flag = 1
            rs += s[i:i+k][::-1]
        
        return rs
