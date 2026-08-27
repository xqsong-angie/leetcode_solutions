#错：
class Solution:
    def cardinalitySort(self,nums):
        mymap={}#🔥如果数组中有重复，新的card会覆盖旧的card, 关键是会丢失有多少个重复的信息
        for i in range(len(nums)):
            card=0
            pt=nums[i]
            while pt>0:
                card+=pt%2
                pt=pt//2
            mymap[nums[i]]=card
        return sorted(mymap.keys()) #🔥不能按照键排序，要先按照值排
    
#对：
class Solution:
    def cardinalitySort(self, nums: list[int]) -> list[int]:
        def get_cardinality(n: int) -> int:
            card = 0
            while n > 0:
                card += n % 2
                n //= 2
            return card

        # 🔥key 返回 (cardinality, 原数值) 的元组，实现两级排序
        return sorted(nums, key=lambda x: (get_cardinality(x), x))