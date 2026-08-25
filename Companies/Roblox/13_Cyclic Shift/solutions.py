#20260823
#不会
from collections import defaultdict

def solution(a: list[int]) -> int:#🔥核心在于转化为最小表示
    def get_min_representation(num: int) -> str:
        s = str(num)
        n = len(s)
        # 生成所有循环移位，并找到字典序最小的字符串
        # s[i:] + s[:i] 即为移位 i 次后的字符串
        return min(s[i:] + s[:i] for i in range(n))

    counts = defaultdict(int)
    pairs = 0

    for num in a:
        key = get_min_representation(num)#每个都算最小表示
        # 如果之前出现过相同的最小表示，直接累加匹配数
        pairs += counts[key]
        counts[key] += 1

    return pairs