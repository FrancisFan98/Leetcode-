class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        rs = [0,0,0,0]
        s = "UDLR"
        
        for cha in moves:
            rs[s.find(cha)] += 1
            
        if rs[0] == rs[1] and rs[2] == rs[3]:
            return True
        return False
