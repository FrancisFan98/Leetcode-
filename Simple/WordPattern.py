class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ans = {}
        chars = pattern
        if not pattern:
            return False
        
        for word in str.split(" "):
            
            while chars and chars[0] in ans:
                chars = chars[1:] 
            
            if not chars:
                break
            
            if word not in ans.values():
                ans[chars[0]] = word
                chars = chars[1:]
        
        if len(ans) != len(set(pattern)):
            print (ans, pattern)
            return False
        
        check = []
        for i in pattern:
            check.append(ans[i])
            
        check = " ".join(check)
        return check == str
        
