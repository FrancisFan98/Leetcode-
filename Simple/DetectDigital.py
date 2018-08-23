class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.islower() | word.isupper():
            return True
        else:
            return word[0].isupper() & word[1:].islower()
        
