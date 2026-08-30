class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        minIndex = nums.index(min(nums))
        maxIndex = nums.index(max(nums))

        left = min(minIndex, maxIndex)
        right = max(minIndex, maxIndex)

        fromFront = right + 1
        fromBack = n - left
        fromBoth = left + 1 + n - right

        return min(fromFront, fromBack, fromBoth)