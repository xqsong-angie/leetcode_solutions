#20260618
#错：
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        a_str=str(a)
        b_str=str(b)
        i=j=0
        while i<len(a_str) and j<len(b_str):
            if int(a_str[i])>int(a_str[j]):
                return a
            elif int(a_str[i])<int(a_str[j]): 
                return b
            else:
                i+=1
                j+=1
        return a if i==len(a_str) else b ##3 34 情况会出错

    def mergeSort(self,nums):#https://www.geeksforgeeks.org/dsa/merge-sort/
        n=len(nums)
        if n==1:
            return nums
        else:
            split=n//2
            left=self.mergeSort(nums[:split])
            right=self.mergeSort(nums[split:])
            i=j=0
            res=[]
            while i<len(left) and j<len(right):
                if self.larger(left[i],right[j])==left[i]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
                if i<n:
                    res.extend(left[i:])
                else:
                    res.extend(right[j:])
                    return res

    def largestNumber(self, nums: List[int]) -> str:#https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
        return "".join(str(s) for s in self.mergeSort(nums))
    
#对：
class Solution:
    def larger(self,a,b):
        return a if int(str(a) + str(b)) > int(str(b) + str(a)) else b


    def mergeSort(self,nums):#https://www.geeksforgeeks.org/dsa/merge-sort/
        n=len(nums)
        if n==1:
            return nums
        else:
            split=n//2
            left=self.mergeSort(nums[:split])
            right=self.mergeSort(nums[split:])
            i=j=0
            res=[]
            while i<len(left) and j<len(right):
                if self.larger(left[i],right[j])==left[i]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1

            res.extend(left[i:])#这里不要判断逻辑，如果有没走完的自然会接，否则接的是空数组
            res.extend(right[j:])
            return res

    def largestNumber(self, nums: List[int]) -> str:#https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
        res="".join(str(s) for s in self.mergeSort(nums)) 
        return "0" if res[0] == "0" else res#修复"00"情况
