class Solution:
    def findTheRank(self,performance,rank):
        performance.sort(key=lambda x:sum(x))#🔥需要倒序排，且maintaining order of students with equal total marks.
        return performance[rank]#🔥rank是1-based index, 不能直接用来当索引

class Solution:
    def findTheRank(self, performance, rank):
        # 带上原始索引 i，元素变成 (i, [成绩列表])
        indexed_perf = list(enumerate(performance))
        
        # 按 (-总分, 原始索引) 排序
        indexed_perf.sort(key=lambda x: (-sum(x[1]), x[0]))
        """
        [
    (0, [79, 89, 15]),  # 第 0 个元素
    (1, [85, 89, 92]),  # 第 1 个元素
    (2, [71, 96, 88])   # 第 2 个元素
]"""
        # 返回第 rank 名的原始索引 x[0]
        return indexed_perf[rank - 1][0]
