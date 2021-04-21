# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        
        new_interval = sorted(intervals, key=lambda pair: pair[1])
        overlap_cnt = 1
        int_end = new_interval[0][1]
        
        # calculate overlapping intervals
        for i in range(1, len(new_interval)):
            if new_interval[i][0] >= int_end:
                int_end = new_interval[i][1]
                overlap_cnt += 1
        
        #subtract overlapping from total intervals to get non-overlapping 
        return len(intervals) - overlap_cnt