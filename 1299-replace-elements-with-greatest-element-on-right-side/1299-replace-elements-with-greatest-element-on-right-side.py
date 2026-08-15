class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [-1] * n
        maxval = arr[n - 1]

        for i in range(n - 2, -1, -1):
            ans[i] = maxval
            maxval = max(arr[i], maxval)

        return ans 