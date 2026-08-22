class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum = 0
        product = 1
        temp = n
        while n:
            t = n % 10
            sum += t
            product *= t
            n = n // 10
        return temp % (sum + product) == 0
