class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammatic = ["0", "1", "6", "9", "8"]
        rever = ["0", "1", "9", "6", "8"]
        reference = dict(zip(strobogrammatic, rever))
        
        first, last = 0, len(num)
        
        while first < last:
            if num[first] not in reference or num[last-1] not in reference:
                return False
            if reference[num[first]] != num[last-1]:
                return False
            first += 1
            last -= 1
        return True