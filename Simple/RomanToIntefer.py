class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rs = 0
        I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
        levels = ["I", "V", "X", "L", "C", "D", "M"]
        nums = dict(zip(levels, [1, 5, 10, 50, 100, 500, 1000]))
        level = 0
        
        for letter in s[::-1]:
            if nums[letter] > nums[levels[level]]:
                rs += nums[letter]
                if level < len(levels)-1:
                    level = levels.index(letter)
            elif nums[letter] == nums[levels[level]]:
                rs += nums[letter]
            else:
                rs -= nums[letter]
        
        return rs
