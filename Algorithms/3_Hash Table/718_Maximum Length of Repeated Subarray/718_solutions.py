#20260805
#https://lush93md.medium.com/leetcode-718-maximum-length-of-repeated-subarray-8c1decea4ddf
class Solution:
    def rollingHash(self, nums: List[int], length: int) -> list[int]:
        P = 101 #进制数（通常选择质数）
        MOD = pow(2, 64)
        hash_list = [0 for _ in range(len(nums) - length + 1)]
        if length == 0:
            return hash_list
        hash = 0
        power = 1
        for i in range(len(nums)):
            if i < length - 1:#窗口还没满
                hash = (hash * P + nums[i]) % MOD#把当前数字加上
                power = (power * P) % MOD #被执行length-1次，范围i=0一直到i=length-2, step=1,最终power=P^(length-1),这就是最高位权重
            else:
                hash_list[i - (length - 1)] = (hash * P + (nums[i]) % MOD ) % MOD#把最后一位加上
                hash = (
                    hash_list[i - (length - 1)] - nums[i - (length - 1)] * power
                ) % MOD

        return hash_list

    def checkLength(self, nums1: List[int], nums2: List[int], length: int) -> bool:#查询两个数组里有没有length长度的LCS
        hash_starting_indexes = {}
        for idx, hash in enumerate(self.rollingHash(nums1, length)):#使用rolling hash存入哈希值，是为了减少空间消耗
            indexes = hash_starting_indexes.get(hash, []) #hash是nums1中所有长度为length的子数组的哈希值
            indexes.append(idx)
            hash_starting_indexes[hash] = indexes#算出来的值存入dict

        for idx2, hash in enumerate(self.rollingHash(nums2, length)):
            for idx1 in hash_starting_indexes.get(hash, []):
                retult = nums1[idx1 : idx1 + length] == nums2[idx2 : idx2 + length]#二次校验
                if retult:
                    return True
        return False

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        lo, hi = 0, min(len(nums1), len(nums2)) + 1 #二分答案的连续范围，公共子数组的可能长度，左闭右开区间
        while lo < hi:
            mid = lo + ((hi - lo) >> 1) #>>1相当于除以2，速度更快
            if self.checkLength(nums1=nums1, nums2=nums2, length=mid):#验证如果公共长度为mid的子数组存在
                lo = mid + 1#说明还可以猜更长的长度
            else:#否则只能猜更小的长度
                hi = mid
        return lo - 1#因为 lo 最终会停在“第一个不合法的长度”上，所以减去 1 就是我们要的“最大合法长度”。