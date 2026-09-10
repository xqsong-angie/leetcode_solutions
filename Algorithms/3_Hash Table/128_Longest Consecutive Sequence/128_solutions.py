#20260727
#错：
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited=set()
        n=len(nums)
        count=1
        for i in range(n):
            if nums[i] not in visited and (nums[i]-1 in visited or nums[i]+1 in visited):
                count+=1
            else:
                visited.add(nums[i]+1)#🔥不能保证 nums[i]+1 nums[i]-1一定在原数组里
                visited.add(nums[i]-1)
            visited.add(nums[i])
        return count

#对：
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # 去重 + O(1) 查找
        longest_streak = 0

        for num in num_set:
            # 只有当 num 是连续序列的起点时（即 num - 1 不存在）才开始计算
            if num - 1 not in num_set: #🔥说明num就是某个序列的第一位
                current_num = num
                current_streak = 1

                # 顺藤摸瓜往后找连续的数字
                while current_num + 1 in num_set:#🔥只有序列起点才会进入 while，所以平摊下来是O(n)
                    current_num += 1
                    current_streak += 1

                # 更新最大长度
                longest_streak = max(longest_streak, current_streak)

        return longest_streak