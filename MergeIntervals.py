# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_interval = sorted(intervals, key=lambda pair:pair[0])
        curr = sorted_interval[0]
        ans = []
        for i in range(1, len(sorted_interval)):
            interval = sorted_interval[i]
            if curr[1] < interval[0]:
                ans.append(curr)
                curr = interval
            else:
                curr[1] = max(curr[1], interval[1])
        ans.append(curr)
        return ans