class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(half):
            if num[i] == "?":
                left_q += 1
            else:
                left_sum += int(num[i])
        
        for i in range(half, n):
            if num[i] == "?":
                right_q += 1
            else:
                right_sum += int(num[i])

        if (left_q - right_q) % 2 != 0:
            return True

        # Difference in the number of ? is even
        q_diff = left_q - right_q
        sum_diff = left_sum - right_sum

        # Each pair of ? can create a difference of 9
        if q_diff > 0:
            return sum_diff + (q_diff // 2) * 9 != 0
        else:
            return sum_diff - ((-q_diff) // 2) * 9 != 0