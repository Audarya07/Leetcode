# Input: timeSeries = [1,4], duration = 2
# Output: 4
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
# Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.

#-------------------------------------------------------------------------------

# Input: timeSeries = [1,2], duration = 2
# Output: 3
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
# Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.

# Greedy Solution
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        cnt = 0
        n = len(timeSeries)
        if n == 0:
            return 0
        
        for i in range(n-1):
            cnt += min(timeSeries[i+1]-timeSeries[i], duration)
        return cnt + duration
        