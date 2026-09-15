from collections import Counter
def solution(customers,products,tags):
    n=len(customers)
    m=len(products)
    mymap=Counter(products)
    for i in range(n):
        for j in range(m):
            mymap[tags[i][j]]+=1
    mytuples=[(k,v) for k,v in mymap]
    mytuples.sort(key=lambda x:(x[1],x[0]))
    return mytuples
    
    
from collections import Counter

def solution(N, M, tags):
    # 1. 找出被所有 N 个顾客都购买过的商品（求所有顾客商品集合的交集）
    common_products = set(tags[0])
    for i in range(1, N):
        common_products.intersection_update(set(tags[i]))
    
    # 如果没有所有顾客共有的商品，返回空
    if not common_products:
        return ""
    
    # 2. 统计所有顾客包裹中所有商品的出现总频次
    flat_tags = [item for sublist in tags for item in sublist]
    freq_map = Counter(flat_tags)
    
    # 3. 找出共有商品中的最高频次
    max_freq = max(freq_map[prod] for prod in common_products)
    
    # 4. 提取频次等于 max_freq 的共有商品
    result = [prod for prod in common_products if freq_map[prod] == max_freq]
    
    # 5. 按字典序/数值升序排序
    result.sort()
    
    # 6. 返回空格分隔的字符串
    return " ".join(map(str, result))

# ==================== 样例测试 ====================
if __name__ == "__main__":
    N, M = 4, 4
    tags = [
        [8, 2, 3, 2],
        [2, 3, 4, 8],
        [8, 3, 11, 12],
        [2, 3, 6, 8]
    ]
    # 输出应为: 3 8
    print(solution(N, M, tags))