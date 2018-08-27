class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        rs = []
        
        for word in words:
            s = set(word.lower())
            for row in rows:
                if s | row == row:
                    rs.append(word)
        return rs
