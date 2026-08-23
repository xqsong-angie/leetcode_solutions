#20260822

from collections import Counter

#不会❌
def solution(numbers):
    # 找到最大长度，统一补前导零（例如：'23' -> '0023'，确保交换时对齐）
    # 如果题目保证数字位数相同或按纯数值/字符串匹配，可据此微调
    max_len = max(len(str(x)) for x in numbers)

    freq_map = Counter()
    ans = 0

    for num in numbers:
        # 转为固定长度的字符串
        s = list(str(num).zfill(max_len))#补充前导0至max_len长度

        # 用 Set 收集当前数字通过“最多换 2 个字符”能变成的所有不同字符串🔥最多交换一次
        possible_variants = set()

        # 情况 1：不交换
        possible_variants.add("".join(s))

        # 情况 2：恰好交换两个位置🔥这里其实就是很简单的双层循环枚举
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n):
                s[i], s[j] = s[j], s[i]  # 交换
                possible_variants.add("".join(s))
                s[i], s[j] = s[j], s[i]  # 还原

        # 在哈希表中查找之前有多少匹配的数字
        for variant in possible_variants:
            if variant in freq_map:
                ans += freq_map[variant]

        # 将当前数字的原型记录进哈希表
        original_str = "".join(s)
        freq_map[original_str] += 1

    return ans