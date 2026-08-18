class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = {}

        for i in range(n - k + 1):
            seen = set()
            for j in range(i, i + k):
                if nums[j] not in seen:
                    seen.add(nums[j])

            for j in seen:
                freq[j] = freq.get(j, 0) + 1
        
        maxnum = -1 
        for num, count in freq.items():
            if count == 1:
                maxnum = max(maxnum, num)
        return maxnum