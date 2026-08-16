class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count_rem = [0] * 3

        for val in stones:
            count_rem[val % 3] += 1

        if count_rem[1] == 0 and count_rem[2] == 0:
            return False

        if count_rem[0] % 2 == 0:
            return count_rem[1] > 0 and count_rem[2] > 0
            
        return abs(count_rem[1] - count_rem[2]) > 2 
