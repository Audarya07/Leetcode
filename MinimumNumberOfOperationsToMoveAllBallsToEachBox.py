# Input: boxes = "110"
# Output: [1,1,3]
# Explanation:
# 1) First box: you will have to move one ball from the second box to the first box in one operation.
# 2) Second box: you will have to move one ball from the first box to the second box in one operation.
# 3) Third box: you will have to move one ball from the first box to the third box in two operations, 
#               and move one ball from the second box to the third box in one operation.


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        leftCount, leftCost = 0, 0
        rightCount, rightCost = 0, 0
        n = len(boxes)
        ans = [0]*n
        for i in range(1, n):
            if boxes[i-1] == '1':
                leftCount += 1
            leftCost += leftCount 
            ans[i] = leftCost
            
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1': 
                rightCount += 1
            rightCost += rightCount
            ans[i] += rightCost
            
        return ans