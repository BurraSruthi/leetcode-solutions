class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        for i in range(1, n + 2):
            if k * i not in nums:
                return k * i
