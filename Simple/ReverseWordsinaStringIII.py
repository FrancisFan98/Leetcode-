class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        s = list(map(reversed, s))
        return " ".join([''.join(word) for word in s])
