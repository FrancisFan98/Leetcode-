class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        
        rs = []
        for op in ops:
            if op == "C" and rs:
                rs.pop()
            elif op == "D" and rs:
                rs.append( 2*int(rs[-1]))
            elif op == '+' and len(rs) >= 2:
                rs.append(int(rs[-1]) + int(rs[-2]))
            else:
                rs.append(int(op))
        return sum(rs)
