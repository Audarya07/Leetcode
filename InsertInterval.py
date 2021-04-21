# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]

class Solution:
    def insert(self, pair: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # Solution 1: O(nlogn)
        # intervals.append(newInterval)
        # new_interval = sorted(intervals, key=lambda pair: pair[0])
        # ans = []
        # for curr_pair in new_interval:
        #     if ans and ans[-1][1] >= curr_pair[0]:
        #         ans[-1][1] = max(ans[-1][1], curr_pair[1])
        #     else:
        #         ans.append(curr_pair)
        # return ans
        

        # Solution 2: O(n)
        ans = []
        i = 0

        # add all the intervals ending before newInterval starts
        while i < len(pair) and pair[i][1] < newInterval[0]:
            ans.append(pair[i])
            i += 1
        
        # merge all overlapping intervals into one considering newInterval
        while i < len(pair) and pair[i][0] <= newInterval[1]:
            newInterval = [min(pair[i][0], newInterval[0]), max(pair[i][1], newInterval[1])]
            i += 1
        ans.append(newInterval)
        
        while i < len(pair):
            ans.append(pair[i])
            i += 1
        return ans