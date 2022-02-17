class Solution:
    def digit_sum(self, num):
        if num == 0:
            return 0
        else:
            return (num%10) + self.digit_sum(num//10)
        
    def countEven(self, num: int) -> int:
        cnt = 0
        for i in range(1, num+1):
            if self.digit_sum(i) % 2 == 0:
                cnt += 1
        return cnt
