class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        self.path=[]
        self.res.append([])
        def backtracking(pt)->None:  
            for i in range(pt,len(nums)):
                self.path.append(nums[i])
                self.path.extend([])
                backtracking(i+1)
                self.res.append(list(self.path)) #注意收集结果位置不一样啦，不再是到数组结束位置，子集问题是每个节点都有结果收集
                self.path.pop()

        backtracking(0)
        return self.res

