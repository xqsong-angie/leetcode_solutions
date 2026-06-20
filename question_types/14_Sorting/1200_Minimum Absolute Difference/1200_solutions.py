#20260619
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_ab_diff=2*10**6
        arr.sort()
        n=len(arr)
        for i in range(1,n):
            min_ab_diff=min(min_ab_diff,arr[i]-arr[i-1])

        res=[]
        for i in range(1,n):
            if arr[i]-arr[i-1]==min_ab_diff:
                res.append([arr[i-1],arr[i]])
        return res