class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        rever = list(reversed(digits))
        for i in range(len(rever)):
            if i == len(rever) -1 and rever[i] == 10:
                rever.append(0)
                
            if rever[i] == 10:
                rever[i] = 0
                rever[i + 1] += 1
        return list(reversed(rever))
