class Solution:
    def maxProduct(self, n: int) -> int:
        lst = []
        while n > 0:
            lst.append(n % 10)
            n = n // 10

        maxproduct = 0
        for i in range(len(lst)):
            for j in range(i + 1,len(lst)):
                maxproduct = max(maxproduct, lst[i] * lst[j])
        return maxproduct
