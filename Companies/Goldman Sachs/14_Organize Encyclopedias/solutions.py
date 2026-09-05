#没思路
#🔥最少选择次数 = 图中连通块的总数量
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))#还是一开始给每一个都分开单独成块
        self.count = n#🔥记录连通块的数量

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.count -= 1

def min_operations(grid):
    if not grid or not grid[0]:
        return 0
    
    n = len(grid)
    m = len(grid[0])
    
    dsu = DSU(n * m)
    
    # 记录每行/每列中，各个作者上一次出现的节点索引
    row_author_map = [{} for _ in range(n)]
    col_author_map = [{} for _ in range(m)]
    
    for r in range(n):
        for c in range(m):
            author = grid[r][c]
            curr_id = r * m + c
            
            # 检查同行同作者
            if author in row_author_map[r]:
                dsu.union(curr_id, row_author_map[r][author])#同行同作者要union
            else:
                row_author_map[r][author] = curr_id#当前行第一次出现该作者，就把该作者的id存放在当前行
                
            # 检查同列同作者
            if author in col_author_map[c]:
                dsu.union(curr_id, col_author_map[c][author])
            else:
                col_author_map[c][author] = curr_id
                
    return dsu.count

# 样例验证
grid = [
    [2, 2, 1],
    [1, 1, 1],
    [2, 3, 3]
]

print(min_operations(grid))  # 输出: 3