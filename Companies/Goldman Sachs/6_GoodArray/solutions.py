def answer_queries(N: int, queries: list[list[int]]) -> list[int]:
    # 1. 提取 N 中所有 2 的幂次的指数 (powers)
    powers = [] 
    #任何正整数 N 都可以唯一地拆解为不同 2 的幂次之和
    #正好对应 N 的二进制二进制表示中为 1 的各个位
    bit = 0
    while N > 0:
        if N & 1:#检查最低位是否是1
            powers.append(bit)
        N >>= 1
        bit += 1

    results = []
    
    # 2. 依次处理每个 query (注意：1-based 索引转换为 0-based)
    for l, r, m in queries:
        # 累加区间内的指数（幂乘等于指数加）
        exp_sum = sum(powers[l - 1 : r])
        
        # 计算 2^exp_sum % m
        ans = pow(2, exp_sum, m)
        results.append(ans)

    return results

# 测试 Example
N = 26
queries = [[1, 2, 1009], [3, 3, 5]]
print(answer_queries(N, queries))  # 输出: [16, 1]
