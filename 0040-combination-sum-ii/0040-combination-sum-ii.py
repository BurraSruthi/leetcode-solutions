class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        n=len(candidates)
        candidates.sort()
        def helper(index,subarray):
            if sum(subarray)>target:
                return
            if sum(subarray)==target:
                res.append(subarray[:])
                return 
            hash={}
            for j in range(index,n):
                if candidates[j] not in hash:
                    hash[candidates[j]]=True
                    subarray.append(candidates[j])
                    helper(j+1,subarray)
                    subarray.pop()
        helper(0,[])
        return res