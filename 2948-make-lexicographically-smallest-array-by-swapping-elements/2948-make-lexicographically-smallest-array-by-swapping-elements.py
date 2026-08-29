class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        # Sort values along with their original indices
        arr = sorted((nums[i], i) for i in range(n))

        groups = []
        current = []

        for i in range(n):
            if i == 0 or arr[i][0] - arr[i - 1][0] <= limit:
                current.append(arr[i])
            else:
                groups.append(current)
                current = [arr[i]]

        groups.append(current)

        ans = nums[:]

        # For every group
        for group in groups:
            # Values are already sorted
            values = [x[0] for x in group]

            # Indices sorted
            indices = sorted(x[1] for x in group)

            # Put smallest value at smallest index
            for i in range(len(group)):
                ans[indices[i]] = values[i]

        return ans