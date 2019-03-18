# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution:
    def canAttendMeetings(self, intervals: 'List[Interval]') -> 'bool':
        end = float('-inf')
        intervals.sort(key=lambda l: l.start)
        for interval in intervals:
            if interval.start < end:
                return False
            else:
                end = interval.end
        return True