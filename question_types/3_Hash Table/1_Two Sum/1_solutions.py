class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymatch={}
        res=[]
        for i in range(len(nums)):
            gap=target-nums[i]
            if gap in mymatch.keys() and mymatch[gap]!=i:
                res.append(i)
                res.append(mymatch[gap])
                return res
            mymatch[nums[i]]=i
        return []

#20260605
class Solution:
    #https://medium.com/@AlexanderObregon/solving-the-two-sum-problem-on-leetcode-python-answer-s-walkthrough-f0c737fb3648
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return [numMap[complement], i]
            numMap[num] = i
        return []
