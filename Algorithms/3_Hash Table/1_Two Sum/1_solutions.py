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

#20260709看了一遍

#20260802
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i in range(len(nums)):
            if target-nums[i] not in hash_map:
                hash_map[nums[i]]=i
            else:
                return [hash_map[target-nums[i]],i]