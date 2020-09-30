class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        summ = 0
        while n:
            rem = n % 10
            mul *= rem
            summ += rem
            n //= 10
        return mul - summ