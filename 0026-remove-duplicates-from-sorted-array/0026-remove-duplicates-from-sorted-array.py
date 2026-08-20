class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 

        first = 1
        second = 1

        for first in range(1, n):
            if nums[first] != nums[first - 1]:
                nums[second] = nums[first]
                second += 1
        return second
