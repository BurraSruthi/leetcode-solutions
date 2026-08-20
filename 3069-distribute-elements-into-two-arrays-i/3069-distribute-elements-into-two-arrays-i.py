class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []

        for i in range(len(nums)):
            if i % 2 == 0:
                if arr1 and arr2:
                    if arr2[-1] < arr1[-1]:
                        arr1.append(nums[i])
                    else:
                        arr2.append(nums[i])
                else:
                    arr1.append(nums[i])
            else:
                if arr1 and arr2:
                    if arr2[-1] < arr1[-1]:
                        arr1.append(nums[i])
                    else:
                        arr2.append(nums[i])
                else:
                    arr2.append(nums[i])

        return arr1 + arr2
