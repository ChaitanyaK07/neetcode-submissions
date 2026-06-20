"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:


        for i in range(len(intervals)):
            for j in range(len(intervals)-i-1):
                if intervals[j].start > intervals[j+1].start:
                    intervals[j], intervals[j+1] = intervals[j+1], intervals[j]
        
        ans = False

        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return ans

        return True
